from typing import List
from .attributes import HTMLAttribute
from .base import HTMLContainerBase, ListBase

class HTMLContainerList(ListBase[HTMLContainerBase]):
    def __str__(self):
        return ''.join(str(x) for x in self)



class HTMLAttributesList(ListBase[HTMLAttribute]):
    def __str__(self):
        return ' '.join(str(x) for x in self)
