# Monitoring Stack with Prometheus, Grafana & Alertmanager

Necessary tools:
===
- Docker
- Docker-compose

Stack overview
===
Prometheus
---
Time Series Database for metrics based monitoring

Grafana
---
Visualization of Prometheus data

Alertmanager
---
Alerting based on Prometheus data


How-to start
===
1. build the images:
``` bash
docker-compose build
```

2. start all necessary images
``` bash
docker-compose up
```