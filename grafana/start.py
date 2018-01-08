#!/usr/bin/python

import requests
from os import environ
from time import sleep
from urlparse import urlunparse
from subprocess import Popen, PIPE


class Grafana(object):
    env = environ.get
    scheme = "http"
    api_path = "api/datasources"

    def __init__(self):
        '''
            Init params
        '''
        self.params = {
            "name": self.env("DS_NAME", "Test datasource"),
            "type": self.env("DS_TYPE", "graphite"),
            "access": self.env("DS_ACCESS", "proxy"),
            "url": self.env("DS_URL", ""),
            "password": self.env("DS_PASS", ""),
            "user": self.env("DS_USER", ""),
            "database": self.env("DS_DB", ""),
            "basicAuth": self.env("DS_AUTH", 'false'),
            "basicAuthUser": self.env("DS_AUTH_USER", ""),
            "basicAuthPassword": self.env("AUTH_PASS", ""),
            "isDefault": self.env("DS_IS_DEFAULT", 'false'),
            "jsonData": self.env("DS_JSON_DATA", 'null')
        }
        # Create grafana api path
        self.gf_url = urlunparse(
            (
                self.scheme,
                ":".join((self.env("GF_HOST", "localhost"), self.env("GF_PORT", "3000"))),
                self.api_path, "", "", ""
            )
        )
        # Init requests session
        self.auth = self.env("GF_USER", "admin"), self.env("GF_PASS", "admin")
        self.sess = requests.Session()

    def init_datasource(self):
        '''
            Upload a datasource
            :return bool
        '''
        response = False
        res = self.sess.post(self.gf_url, data=self.params, auth=self.auth)
        if res.status_code == requests.codes.ok:
            response = True

        return response

    def start(self):
        '''
            Start grafana and check api
            :return tuple - status, grafana process
        '''
        status = False
        # run grafana
        gf_proc = Popen([
            "/usr/sbin/grafana-server",
            "--homepath=/usr/share/grafana",
            "--config=/etc/grafana/grafana.ini",
            "cfg:default.paths.data=/var/lib/grafana",
            "cfg:default.paths.logs=/var/log/grafana"],
            stdout=PIPE
        )
        # wait, until gf api will be available
        # trying 5 times
        retry = 0
        while retry <= 5:
            if self._check_gf():
                status = True
                break
            retry += 1
            sleep(3)

        return status, gf_proc

    def _check_gf(self):
        '''
            Check gf api
            :return bool
        '''
        resp = False
        try:
            res = self.sess.get(self.gf_url, auth=self.auth)
            resp = True if res and res.status_code == requests.codes.ok else False
        except Exception as message:
            print "CONNECTION! %s" % message

        return resp


if __name__ == "__main__":
    gf = Grafana()
    try:
        exit_code = 0
        status, gf_proc = gf.start()
        if status:
            if gf.init_datasource():
                print "*------------SUCCESS! Your datasource was added!------------*"
                while True:
                    # read gf stdout until it terminated
                    output = gf_proc.stdout.readline()
                    if output == '' and gf_proc.poll() is not None:
                        break
                    if output:
                        print output.strip()
                    sleep(3)

            exit_code = gf_proc.poll()
    except Exception as error:
        print "*------------ERROR! %s------------*" % error
        exit_code = 1
    finally:
        exit(exit_code)
