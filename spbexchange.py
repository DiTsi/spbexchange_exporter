from bs4 import BeautifulSoup
from urllib import request
import sys


url = 'http://spbexchange.com/en/market_data/'
table_cols = 11


class Stock:
    def __init__(self, ticker, name='None', cur='-', ch_to_prev_close='-', open='-',
                low='-', high='-', last='-', ch_to_prev_close_2='-', bid='-',
                offer='-') -> None:
        self.ticker = ticker
        self.name = name
        self.cur = cur
        self.ch_to_prev_close = ch_to_prev_close
        self.open = open
        self.low = low
        self.high = high
        self.last = last
        self.ch_to_prev_close_2 = ch_to_prev_close_2
        self.bid = bid
        self.offer = offer


def get_table():
    page_source = request.urlopen(url).read()
    soup = BeautifulSoup(page_source, "html.parser")
    try:
        table = soup.find("table", attrs={'border': '1'})
    except Exception:
        print("Error parsing site")
        sys.exit('Error parsing site')

    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [el.text.strip() for el in cols]
        if len(cols) == table_cols:
            obj = Stock(
                ticker=cols[0],
                name=cols[1],
                cur=cols[2],
                ch_to_prev_close=cols[3],
                open=cols[4],
                low=cols[5],
                high=cols[6],
                last=cols[7],
                ch_to_prev_close_2=cols[8],
                bid=cols[9],
                offer=cols[10]
            )
            data.append(obj)
        else:
            print(f'Error loading row: {cols}')
    return data


def main():
    table = get_table()
    pass


main()
