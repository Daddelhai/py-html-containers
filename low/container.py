from .list import HTMLContainerList, HTMLAttributesList
from .base import HTMLContainerBase

class HTMLContainer(HTMLContainerBase):
    def __init__(self, objtype: str, attributes: HTMLAttributesList = HTMLAttributesList()):
        self.type = objtype
        self.attributes = attributes

    def __str__(self):
        attributes_str = ' '+self.attributes if self.attributes else ''
        return f"<{self.type}{attributes_str}/>"


class ChildableHTMLContainer(HTMLContainer):
    def __init__(self, objtype: str, childs: HTMLContainerList = HTMLContainerList(), attributes: HTMLAttributesList = HTMLAttributesList()):
        self.type = objtype
        self.childs = childs
        self.attributes = attributes

    def __str__(self):
        attributes_str = ' '+self.attributes if self.attributes else ''
        return f"<{self.type}{attributes_str}>{self.childs}</{self.type}>"

    def add_child(self, *childs: HTMLContainerBase):
        for child in childs:
            self.childs.append(child)