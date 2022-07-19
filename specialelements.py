import django.middleware.csrf as csrf
from .low.container import HTMLContainer, ChildableHTMLContainer, Text
from .elements import Input, Option


class DjangoCSRFToken(Input):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.name = "csrfmiddlewaretoken"
        self.attr.value = csrf.get_token(request)
        self.attr.type = "hidden"


class Submit(Input):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "submit"


class Checkbox(Input):
    def __init__(self, checked: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "checkbox"
        if checked:
            self.attr.checked = True


class NumberInput(Input):
    def __init__(self, max=None, min=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "number"
        if max is not None:
            self.attr.max = max
        if min is not None:
            self.attr.min = min


class DateTimeInput(Input):
    def __init__(self, max=None, min=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "datetime"
        if max is not None:
            self.attr.max = max
        if min is not None:
            self.attr.min = min


class DateInput(DateTimeInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "date"


class TimeInput(DateTimeInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "time"


class TextInput(Input):
    def __init__(self, maxlength=None, minlength=None, pattern=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "text"
        if maxlength is not None:
            self.attr.maxlength = maxlength
        if minlength is not None:
            self.attr.minlength = minlength
        if pattern is not None:
            self.attr.pattern = pattern


class PasswordInput(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "password"


class Select(ChildableHTMLContainer):
    def __init__(self, selected=None, label=None, options: dict = None, *args, **kwargs):
        super().__init__("select", *args, **kwargs)

        self.selected = selected

        if self.options is not None:
            self.__populate(self.options)
        elif options is not None:
            self.__populate(options)

        self.label = label

    def __populate(self, items):
        if isinstance(items, dict):
            for value, text in items.items():
                self.add_child(
                    Option(
                        text,
                        value,
                        selected=True if self.selected is not None and self.selected == value else False)
                )
        else:
            for value in items:
                self.add_child(
                    Option(
                        value,
                        value,
                        selected=True if self.selected is not None and self.selected == value else False)
                )

    def __str__(self):
        attributes_str = ' '+str(self.attr) if self.attr else ''
        if self.label is not None:
            return f"<label>{self.label}:<{self._objtype}{attributes_str}>{self.childs}</{self._objtype}></label>"
        return f"<{self._objtype}{attributes_str}>{self.childs}</{self._objtype}>"
