class Headers:
    def __init__(self, headers = {}):
        self.__headers = headers

    def __str__(self) -> str:
        return JSON.stringify(self.__headers)

    def set(self, name: str, value) -> None:
        self.__headers[name] = [value]

    def get(self, name: str):
        return self.__headers.get(name)

    def append(self, name: str, value) -> None:
        if (self.has(name)):
            self.__headers.get(name).push(value)
        else:
            self.set(name, value)

    def has(self, name: str) -> bool:
        return name in self.__headers

    def remove(self, name: str):
        pass
