# Prometheus exporter для [Санкт-Петербургской биржи](https://spbexchange.ru/)

README на других языках: [English](https://github.com/DiTsi/spbexchange_exporter/blob/main/README.md), [Русский](https://github.com/DiTsi/spbexchange_exporter/blob/main/README.ru.md)

## Docker

Запуск exporter'а на 8000 порту:
```
docker run -d -p 8000:4512 ditsi/spbexchange_exporter:latest
```

Чтобы посмотреть метрики, перейдите на http://localhost:8000/
