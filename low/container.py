from .collections import HTMLContainerList, HTMLAttributesDict
from .base import HTMLContainerBase
from .attributes import HTMLClassAttribute
from typing import Optional, Union
from contextlib import contextmanager


class Text(HTMLContainerBase):
    def __init__(self, text: str, style: Optional[dict] = None):
        self.text = text
        self.style = style

    def __str__(self):
        if self.style is None:
            return self.text
        else:
            return '<span style="' + ','.join(f'{x}: {y}' for x, y in self.style.items()) + f'">{self.text}</span>'


class HTMLContainer(HTMLContainerBase):
    def __init__(self, objtype: str, attributes: Optional[HTMLAttributesDict|dict] = None, classes: Optional[HTMLClassAttribute|list] = None):
        self.type = objtype
        self.attr = HTMLAttributesDict(attributes) if attributes is not None else HTMLAttributesDict()
        if classes is not None:
            for cls in classes:
                self.attr["class"] = cls

    def __str__(self):
        attributes_str = ' '+str(self.attr) if self.attr else ''
        return f"<{self.type}{attributes_str}/>"

    @property
    def classes(self) -> HTMLClassAttribute:
        return self.attr["class"]

    @classmethod
    @contextmanager
    def AsChildOf(cls, parent, *args, **kwargs):
        child = cls(*args, **kwargs)
        parent.add_child(child)

        yield child



class ChildableHTMLContainer(HTMLContainer):
    def __init__(self, objtype: str, childs: Optional[HTMLContainerList|dict] = None, attributes: Optional[HTMLAttributesDict|dict] = None, classes: Optional[HTMLClassAttribute|list] = None, text: Optional[str] = None):
        super().__init__(objtype, attributes, classes)
        self.childs = HTMLContainerList(childs) if childs is not None else HTMLContainerList()
        if text is not None:
            self.childs.append(Text(text))

    def __str__(self):
        attributes_str = ' '+str(self.attr) if self.attr else ''
        return f"<{self.type}{attributes_str}>{self.childs}</{self.type}>"

    def add_child(self, *childs: HTMLContainerBase):
        for child in childs:
            self.childs.append(child)

    def text(self, text: str, style: Optional[dict] = None):
        self.add_child(Text(text, style))
        return self
