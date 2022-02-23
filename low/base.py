import abc

class HTMLContainerBase:
    @abc.abstractmethod
    def __str__(self):
        pass

class ListBase:
    def __init__(self, data: list[HTMLContainerBase]=[]):
        self.data = data

    def __delitem__(self, key: int):
        del self.data[key]

    def __getitem__(self, key: int):
        return self.data[key]

    def __setitem__(self, key: int, value: HTMLContainerBase):
        self.data[key] = value

    @abc.abstractmethod
    def __str__(self):
        pass