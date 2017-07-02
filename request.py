# https://docs.python.org/3.0/library/urllib.request.html
# https://developer.mozilla.org/en-US/docs/Web/API/Request
import urllib.request
from shgysk8zer0.pyurlutils.body import Body
from shgysk8zer0.pyurlutils.headers import Headers
from urllib.request import Request as Req

class Request(Req):
    def __init__(self, url: str, opts = {}):
        super().__init__(str(url))
        self.__headers = Headers()
        self.__body = Body()
        self.__url = url
        self.__method = 'GET'
        self.__body_used = false
        # if headers in opts:

    def __str__(self) -> str:
        return self.__url

    def clone(self):
        return copy(self)

    @property
    def headers(self) -> Headers:
        return self.__headers

    @property
    def body(self) -> Body:
        return self.__body

    @property
    def method(self) -> str:
        return self.__method

    @property
    def url(self) -> str:
        return self.__url

    @property
    def bodyUsed(self) -> bool:
        return self.__body_used
