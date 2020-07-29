import requests
import os
from configparser import ConfigParser
from time import sleep
from sys import platform

class SendToServer:

    def __init__(self):
        self.configs = self.config(section="auto_bug_endpoint")
        self.url = self.configs.get("url")

    def config(self, section):
        # Can add more platforms here like windows if needed.
        if platform == 'linux':
            filename = os.path.abspath("resource/config.ini")
        else:
            filename = os.path.abspath("../resource/config.ini")
        parser = ConfigParser()
        parser.read(filename)

        configOptions = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                configOptions[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found on the {1} file '.format(section, filename))

        return configOptions

    def sendToServer(self, traceback):
        sleep(1.5)
        return requests.post(self.url, data=traceback)
