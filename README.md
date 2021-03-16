# Prometheus exporter for [Saint-Petersburg Exchange](http://spbexchange.com/)

Another languages README: [English](https://github.com/DiTsi/spbexchange_exporter/blob/main/README.md), [Русский](https://github.com/DiTsi/spbexchange_exporter/blob/main/README.ru.md)

## Docker

Run exporter on 8000 port:
```
docker run -d -p 8000:4512 ditsi/spbexchange_exporter:latest
```

To see metrics go to http://localhost:8000/
