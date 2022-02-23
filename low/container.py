from .list import HTMLContainerList, HTMLAttributesList
from .base import HTMLContainerBase

class HTMLContainer(HTMLContainerBase):
    def __init__(self, objtype: str, attributes: HTMLAttributesList = []):
        self.type = objtype
        self.attributes = attributes

    def __str__(self):
        return f"<{self.type} {self.attributes}/>"


class ChildableHTMLContainer(HTMLContainer):
    def __init__(self, objtype: str, childs: HTMLContainerList = [], attributes: HTMLAttributesList = []):
        self.type = objtype
        self.childs = childs
        self.attributes = attributes

    def __str__(self):
        return f"<{self.type} {self.attributes}>{self.childs}</{self.type}>"