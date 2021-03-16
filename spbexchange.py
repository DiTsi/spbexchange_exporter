import sys
import re
import os
from time import sleep
from urllib import request
from bs4 import BeautifulSoup
from prometheus_client import start_http_server, Gauge, Summary


url = 'http://spbexchange.com/en/market_data/'
table_cols = 11
UPDATE_DELAY = os.environ('UPDATE_DELAY', 300)


class Stock:
    def __init__(self, ticker, name='None', current_price='-', change_to_previous_close='-', open='-',
                low='-', high='-', last='-', change_to_previous_close_2='-', bid='-',
                offer='-') -> None:
        self.ticker = ticker
        self.name = name
        self.current_price = current_price
        self.change_to_previous_close = change_to_previous_close
        self.open = open
        self.low = low
        self.high = high
        self.last = last
        self.change_to_previous_close_2 = change_to_previous_close_2
        self.bid = bid
        self.offer = offer

    def __str__(self) -> str:
        return(f'ticker: {self.ticker}')

    def float(self, attr):
        val = self.__getattribute__(attr)
        try:
            val = re.sub(',', '.', val)
            return float(val)
        except Exception:
            print(f'Can\'t return value for {self}.{attr}')
            return -1.0
    

def stocks():
    page_source = request.urlopen(url).read()
    soup = BeautifulSoup(page_source, "html.parser")
    try:
        table = soup.find("table", attrs={'border': '1'})
    except Exception:
        print("Error parsing site")
        sys.exit('Error parsing site')

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [el.text.strip() for el in cols]
        if len(cols) == table_cols:
            stock = Stock(
                ticker=cols[0],
                name=cols[1],
                current_price=cols[2],
                change_to_previous_close=cols[3].replace('%', ''),
                open=cols[4],
                low=cols[5],
                high=cols[6],
                last=cols[7],
                change_to_previous_close_2=cols[8].replace('%', ''),
                bid=cols[9],
                offer=cols[10]
            )
            yield stock


def update_metrics():
    for stock in stocks():
        prom_current_price = Gauge(name='current_price', documentation='Current Price, USD', labelnames=('ticker'), labelvalues=stock.ticker)
        prom_change_to_previous_close = Gauge(name='change_to_previous_close', documentation='Change to Previous Close, %', labelnames=('ticker'), labelvalues=stock.ticker)
        prom_open = Gauge(name='open', documentation='Open, USD', labelnames=('ticker'), labelvalues=stock.ticker)
        prom_low = Gauge(name='low', documentation='Low, USD', labelnames=('ticker'), labelvalues=stock.ticker)
        prom_high = Gauge(name='high', documentation='High, USD', labelnames=('ticker'), labelvalues=stock.ticker)
        prom_last = Gauge(name='last', documentation='Last, USD', labelnames=('ticker'), labelvalues=stock.ticker)
        prom_change_to_previous_close_2 = Gauge(name='change_to_previous_close_2', documentation='Change to Previous Close 2, %', labelnames=('ticker'), labelvalues=stock.ticker)
        prom_bid = Gauge(name='bid', documentation='Bid, USD', labelnames=('ticker'), labelvalues=stock.ticker)
        prom_offer = Gauge(name='offer', documentation='Offer, USD', labelnames=('ticker'), labelvalues=stock.ticker)

        prom_current_price.set(stock.float('current_price'))
        prom_change_to_previous_close.set(stock.float('change_to_previous_close'))
        prom_open.set(stock.float('open'))
        prom_low.set(stock.float('low'))
        prom_high.set(stock.float('high'))
        prom_last.set(stock.float('last'))
        prom_change_to_previous_close_2.set(stock.float('change_to_previous_close_2'))
        prom_bid.set(stock.float('bid'))
        prom_offer.set(stock.float('offer'))


def main():
    start_http_server(8000)
    update_metrics()
    sleep(UPDATE_DELAY)


if __name__ == '__main__':
    main()
