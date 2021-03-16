FROM python:3.9-alpine
WORKDIR /app

RUN adduser -G nogroup -D -h /app -u 13563 exchange
USER exchange
COPY . .
RUN pip install --user -r requirements.txt

CMD ["python", "spbexchange.py"]
