#!/usr/local/bin/python3
import docker
client = docker.from_env()

DOCKER_REGISTRY = "localhost:5000"

containersToBuild = ["prometheus", "grafana", "alertmanager"]

for container in containersToBuild:
    print("building docker imager for: " + container)
    client.images.build(path=container, tag=DOCKER_REGISTRY + "/" + "obi/" + container + ":1.0")
    print("Push Image to Docker Registry")

    for line in client.images.push(DOCKER_REGISTRY + "/" + "obi/" + container, stream=True):
      print(line)