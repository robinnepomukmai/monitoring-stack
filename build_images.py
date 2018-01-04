import docker
client = docker.from_env()

containersToBuild = ["prometheus", "grafana", "alertmanager"]

for container in containersToBuild:
    print("building docker imager for: " + container)
    client.images.build(path=container, tag=container)
