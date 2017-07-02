from urllib.parse import parse_qsl
class SearchParams:
    def __init__(self, params: str):
        self.__params = dict(parse_qsl(params))

    def __str__(self) -> str:
        return urlencode(self.__params)

    def set(self, name: str, value):
        self.__params[name] = value

    def append(self, name: str, value):
        pass

    def get(self, name: str):
        if self.has(name):
            return self.__params[name]
        else:
            return ''

    def has(self, name: str) -> bool:
        return name in self.__params

    def delete(self, name: str):
        if self.has(name):
            del self.__params[name]

    def keys(self):
        return self.__params.keys()

    def values(self):
        return self.__params.values()

    def entries(self):
        return self.__params.items()

    def debug(self):
        help(self)
