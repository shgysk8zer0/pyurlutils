from json import loads
from http.client import HTTPResponse
from shgysk8zer0.pyurlutils.formdata import FormData

class Body:
    def __init__(self, resp: HTTPResponse):
        self.__resp = resp

    def text(self) -> str:
        return self.__resp.read().decode('utf-8')

    def json(self) -> dict:
        return loads(self.text())

    def arrayBuffer(self):
        pass

    def blob(self):
        pass
