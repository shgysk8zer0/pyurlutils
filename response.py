# https://docs.python.org/3.5/library/http.client.html
# https://developer.mozilla.org/en-US/docs/Web/API/Response
from http.client import HTTPResponse
from shgysk8zer0.pyurlutils.body import Body
from shgysk8zer0.pyurlutils.headers import Headers

class Response:
    def __init__(self, HTTPResponse):
        self.__resp = resp
        self.__body = Body(resp)
        self.__headers = Headers(dict(resp.getheaders()))

    def __str__(self):
        return self.text()

    def arrayBuffer(self):
        return self.__body.arrayBuffer()

    def blob(self):
        return self.__body.blob()

    def clone(self):
        return copy(self)

    def error(self):
        pass

    def formData(self):
        pass

    def json(self) -> dict:
        return JSON.parse(self.text())

    def redirect(self):
        pass

    def text(self):
        return self.__body.text()

    @property
    def url(self) -> str:
        return self.__resp.geturl()

    @property
    def body(self):
        return self.__body

    @property
    def headers(self):
        return self.__headers

    @property
    def status(self) -> int:
        return self.__resp.status

    @property
    def ok(self) -> bool:
        return self.status is 200

    @property
    def statusText(self) -> str:
        return self.__resp.reason
