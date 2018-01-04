#!/usr/local/bin/python3
import docker
client = docker.from_env()

DOCKER_REGISTRY = "localhost:5000"
MONITORING_STACK_VERSION = "1"

containersToBuild = ["prometheus", "grafana", "alertmanager"]

for container in containersToBuild:
    repositoryName = "obi/" + container
    print("building docker imager for: " + repositoryName)
    client.images.build(path=container, tag=DOCKER_REGISTRY + "/" + repositoryName + MONITORING_STACK_VERSION)
    print("Push Image to Docker Registry")

    for line in client.images.push(DOCKER_REGISTRY + "/" + repositoryName, stream=True):
      print(line)