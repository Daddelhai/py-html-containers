from .low.container import HTMLContainer, ChildableHTMLContainer, Text
from .low.base import HTMLContainerBase


class Div(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("div", *args, **kwargs)


class H1(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("h1", *args, **kwargs)


class H2(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("h2", *args, **kwargs)


class H3(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("h3", *args, **kwargs)


class P(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("p", *args, **kwargs)


class Label(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("label", *args, **kwargs)


class A(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("a", *args, **kwargs)


class Img(HTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("img", *args, **kwargs)


class Br(HTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("br", *args, **kwargs)


class Hr(HTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("hr", *args, **kwargs)


class Wbr(HTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("wbr", *args, **kwargs)


class Button(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("button", *args, **kwargs)


class Fieldset(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("fieldset", *args, **kwargs)


class Form(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("form", *args, **kwargs)


class Textarea(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("textarea", *args, **kwargs)


class Grid(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("grid", *args, **kwargs)


class Meta(HTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("meta", *args, **kwargs)


class Title(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("title", *args, **kwargs)


class Head(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("head", *args, **kwargs)


class Body(ChildableHTMLContainer):
    def __init__(self, *args, **kwargs):
        super().__init__("body", *args, **kwargs)


class Input(HTMLContainer):
    def __init__(self, type=None, placeholder=None, readonly=False, required=False, *args, **kwargs):
        super().__init__("input", *args, **kwargs)

        if type is not None:
            self.attr.type = type
        if placeholder is not None:
            self.attr.placeholder = placeholder

        if readonly:
            self.attr.readonly = True
        if required:
            self.attr.required = True


class Option(HTMLContainer):
    def __init__(self, text, value, selected: bool = False, *args, **kwargs):
        super().__init__("option", *args, **kwargs)

        self.text = text
        self.attr.value = value

        if selected:
            self.attr.selected = True

    def __str__(self):
        attributes_str = ' '+str(self.attr) if self.attr else ''
        return f"<{self._objtype}{attributes_str}>{self.text}</{self._objtype}>"


# fmt: off
from .specialelements import *
