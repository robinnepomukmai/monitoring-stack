#!/usr/local/bin/python3
import docker
client = docker.from_env()

DOCKER_REGISTRY = "localhost:5000"
MONITORING_STACK_VERSION = "1"


containersToStart = ["prometheus", "grafana", "alertmanager"]

for service in containersToStart:
    if service == "prometheus":
        ports = {'9090': '9090'}
    if service == "grafana":
        ports = {'3000': '3000'}
    if service == "alertmanager":
        ports = {'9093': '9093'}

    repositoryName = "obi/" + service
    print("starting... " + service)
    dockerOutput = client.containers.run(DOCKER_REGISTRY + "/" + repositoryName + ":" + MONITORING_STACK_VERSION, detach=True, ports=ports, remove=True)
    print(dockerOutput)