from typing import List
from .attributes import HTMLAttribute, HTMLClassAttribute
from .base import HTMLContainerBase, ListBase, DictBase


class HTMLContainerList(ListBase[HTMLContainerBase]):
    def __str__(self):
        if not self._data:
            return ''
        return '' + ''.join(str(x) for x in self._data if x)


class HTMLAttributesDict(DictBase[str, HTMLAttribute]):
    def __init__(self, data: dict[str, str] = None):
        super().__init__()
        if data is not None:
            for key, value in data.items():
                self[key] = value

    def __str__(self):
        if not self._data:
            return ''
        test = ' '.join(str(x) for x in self._data.values() if x)
        return test

    def __setitem__(self, key: str, value):
        if key == "class":
            self._data[key] = HTMLClassAttribute(value.split())
        else:
            self._data[key] = HTMLAttribute(key, value)

    def __setattr__(self, key: str, value: str):
        return self.__setitem__(key, value)

    def __getitem__(self, key: str):
        if key == "class":
            if key in self._data:
                return self._data[key]
            else:
                self._data[key] = HTMLClassAttribute()
                return self._data[key]
        else:
            return self._data[key].value

    def __getattr__(self, key: str):
        return self.__getitem__(key)
