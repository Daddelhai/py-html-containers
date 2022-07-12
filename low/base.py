from typing import TypeVar, Generic
import abc
from contextlib import contextmanager

T = TypeVar('T')
K = TypeVar('K', int, str)


class HTMLContainerBase:
    @abc.abstractmethod
    def __str__(self):
        pass

    @classmethod
    @contextmanager
    def AsChildOf(cls, parent, *args, **kwargs):
        child = cls(*args, **kwargs)
        parent.add_child(child)

        yield child


class ListBase(Generic[T]):
    def __init__(self, data: list[T] = None):
        self._data = list[T](data) if data is not None else list[T]()

    def __delitem__(self, key: int):
        del self._data[key]

    def __getitem__(self, key: int):
        return self._data[key]

    def __setitem__(self, key: int, value: T):
        self._data[key] = value

    def add(self, value: T):
        self._data.add(value)

    def __bool__(self):
        return bool(self._data)

    def __iter__(self):
        for value in self._data:
            yield value

    @abc.abstractmethod
    def __str__(self):
        pass


class DictBase(Generic[K, T]):
    def __init__(self, data: dict[K, T] = None):
        self.__dict__['_data'] = dict[K, T](data) if data is not None else dict[K, T]()

    def __delitem__(self, key: K):
        del self._data[key]

    def __getitem__(self, key: K):
        return self._data[key]

    def __setitem__(self, key: K, value: T):
        self._data[key] = value

    def __delattr__(self, key: str):
        return self.__getitem__(key)

    def __getattr__(self, key: str):
        return self.__getitem__(key)

    def __setattr__(self, key: str, value: T):
        return self.__setitem__(key, value)

    def __bool__(self):
        return bool(self._data)

    def __iter__(self):
        for value in self._data:
            yield value

    @abc.abstractmethod
    def __str__(self):
        pass
