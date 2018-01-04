import docker

GRAFANA_PORT = 3000
PROMETHEUS_PORT = 9090

array(containersToBuild[])

client = docker.from_env()

client.containers.run("ubuntu:latest", "echo hello world")

lol = client.images.build(path="grafana", tag="lol")

print(lol)