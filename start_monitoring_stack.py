#!/usr/local/bin/python3
import docker
client = docker.from_env()

DOCKER_REGISTRY = "localhost:5000"
MONITORING_STACK_VERSION = "1"


containersToStart = ["prometheus", "grafana", "alertmanager"]

for service in containersToStart:
    repositoryName = "obi/" + service
    print("starting... " + service)
    dockerOutput = client.containers.run(DOCKER_REGISTRY + "/" + repositoryName + MONITORING_STACK_VERSION, detach=True)
    print(dockerOutput)