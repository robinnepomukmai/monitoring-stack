# Monitoring Stack with Prometheus, Grafana & Alertmanager

Necessary tools:
===
- Docker3
- Python
- docker-py (pip3 install docker)

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
1. start the local docker registry by execute:
``` bash
python3 start_docker_registry.py
```

2. build and push the docker images
``` bash
python3 build_images.py

```

3. start all necessary images
``` bash
python3 start_monitoring_stack.py
```


Docker Registry foo
===

list all images
---
````bash

http://localhost:5000/v2/_catalog
````

