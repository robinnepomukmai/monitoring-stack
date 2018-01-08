FROM grafana/grafana

#VOLUME ["/var/lib/grafana", "/var/log/grafana", "/etc/grafana"]

RUN apt update -y
RUN apt -y install python python-pip
RUN pip install requests

COPY ./start.py /opt/grafana/start.py
RUN chmod +x /opt/grafana/start.py

#EXPOSE 3000

#ENTRYPOINT ["/opt/grafana/start.py"]
#"curl --user admin:admin 'http://localhost:3000/api/datasources' -X POST -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{\"name\":\"prometheus\",\"isDefault\":true ,\"type\":\"prometheus\",\"url\":\"http://localhost:9090\",\"access\":\"proxy\",\"basicAuth\":false}'"

#curl --user admin:admin 'http://IPADDR:3000/api/datasources' -X POST -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"name":"test","isDefault":true ,"type":"prometheus","url":"http://localhost:9090","access":"proxy","basicAuth":false}'