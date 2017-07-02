from urllib.parse import urlparse
from shgysk8zer0.pyurlutils.searchparams import SearchParams

class URL:
    port = 80
    pathname = '/'
    hash = None
    hostname = None
    password = None
    protocol = ''
    username = None
    searchParams = None

    def __init__(self, url: str, base = None):
        parsed = urlparse(url)
        self.protocol = parsed.scheme
        self.host = parsed.netloc
        self.pathname = parsed.path
        self.anchor = parsed.fragment
        self.searchParams = SearchParams(parsed.query)

    def __str__(self) -> str:
        return self.href

    @property
    def search(self) -> str:
        return self.searchParams

    @search.setter
    def search(self, query: str):
        self.searchParams = SearchParams(query)

    @property
    def href(self) -> str:
        return '{}{}'.format(self.origin, self.pathname)

    @property
    def origin(self) -> str:
        return '{}://{}'.format(self.protocol, self.host)

    @href.setter
    def href(self, value: str):
        self.init(value)

