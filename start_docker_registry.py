#!/usr/local/bin/python3
import os

os.system("docker run -d -p 5000:5000 --restart=always --name registry registry:2")