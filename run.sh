#!/bin/bash

docker build -t lucify-grafana
docker build -t lucify-prometheus
docker build -t lucify-prometheus

docker run -d -p 3000:3000 -e "GF_SECURITY_ADMIN_PASSWORD=admin_password" -v ~/grafana_db:/var/lib/grafana grafana/grafana