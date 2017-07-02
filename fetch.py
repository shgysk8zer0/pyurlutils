from shgysk8zer0.pyurlutils.request import Request
from shgysk8zer0.pyurlutils.response import Response
from urllib.error import URLError, HTTPError
import urllib.request

# TODO make async
def fetch(url: str, opts = {}):
    req = Request(url)
    try:
        req.add_header('Accept', 'application/json')
        return Response(urllib.request.urlopen(req))
    except HTTPError as e:
        print(e)

    except URLError as e:
        print(e)
