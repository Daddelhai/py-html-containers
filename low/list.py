from typing import List
from .attributes import HTMLAttribute
from .base import HTMLContainerBase, ListBase

class HTMLContainerList(ListBase):
    def __init__(self, data: List[HTMLContainerBase]=[]):
        self.data = data

    def __delitem__(self, key: int):
        del self.data[key]

    def __getitem__(self, key: int):
        return self.data[key]

    def __setitem__(self, key: int, value: HTMLContainerBase):
        self.data[key] = value

    def __str__(self):
        return ''.join(self)



class HTMLAttributesList(ListBase):
    def __init__(self, data: List[HTMLAttribute]=[]):
        self.data = data

    def __delitem__(self, key: int):
        del self.data[key]

    def __getitem__(self, key: int):
        return self.data[key]

    def __setitem__(self, key: int, value: HTMLAttribute):
        self.data[key] = value

    def __str__(self):
        return ' '.join(self)
