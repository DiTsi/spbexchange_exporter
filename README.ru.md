# Prometheus exporter для [Санкт-Петербургской биржи](https://spbexchange.ru/)

README на других языках: [English](https://github.com/DiTsi/spbexchange_exporter/blob/main/README.md), [Русский](https://github.com/DiTsi/spbexchange_exporter/blob/main/README.ru.md)

## Docker

### Docker Hub 
[ссылка](https://hub.docker.com/r/ditsi/spbexchange_exporter)

### Запуск

Запуск exporter'а на 8000 порту:
```
docker run -d -p 8000:4512 ditsi/spbexchange_exporter:latest
```

Чтобы посмотреть метрики, перейдите на http://localhost:8000/

### Переменные окружения
- UPDATE_DELAY - задержка между обновлением данных (в секундах)
- EXPORTER_PORT - порт exporter'а. По-умолчанию: 4512
- ADDRESS - IP адрес, на котором слушает сервер. По-умолчанию: 0.0.0.0
