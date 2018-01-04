#!/usr/local/bin/python3
import docker
client = docker.from_env()

DOCKER_REGISTRY = "localhost:5000"

containersToStart = ["prometheus", "grafana", "alertmanager"]

for service in containersToStart:
    print("starting... " + service)
    lol = client.containers.run(DOCKER_REGISTRY + "/" + "obi/" + service + ":1.0", detach=True)
    print(lol)