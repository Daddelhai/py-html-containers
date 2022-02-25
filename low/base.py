from typing import TypeVar, Generic
import abc

T = TypeVar('T')

class HTMLContainerBase:
    @abc.abstractmethod
    def __str__(self):
        pass

class ListBase(Generic[T]):
    def __init__(self, data: list[T]=[]):
        self.data = data

    def __delitem__(self, key: int):
        del self.data[key]

    def __getitem__(self, key: int):
        return self.data[key]

    def __setitem__(self, key: int, value: T):
        self.data[key] = value

    def append(self, value: T):
        self.data.append(value)

    def __bool__(self):
        return bool(self.data)

    def __iter__(self):
        for value in self.data:
            yield value

    @abc.abstractmethod
    def __str__(self):
        pass