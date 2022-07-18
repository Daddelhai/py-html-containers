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
    def __init__(self, value=None, max=None, min=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "number"
        if value is not None:
            self.attr.value = value
        if max is not None:
            self.attr.max = max
        if min is not None:
            self.attr.min = min


class DateTimeInput(Input):
    def __init__(self, value=None, max=None, min=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "datetime"
        if value is not None:
            self.attr.value = value
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
    def __init__(self, value=None, maxlength=None, minlength=None, pattern=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "text"
        if value is not None:
            self.attr.value = value
        if maxlength is not None:
            self.attr.max = maxlength
        if minlength is not None:
            self.attr.min = minlength
        if pattern is not None:
            self.attr.pattern = pattern


class PasswordInput(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "password"


class Select(ChildableHTMLContainer):
    def __init__(self, selected=None, options: dict = None, *args, **kwargs):
        super().__init__("select", *args, **kwargs)

        self.selected = selected

        if self.options is not None:
            self.__populate(self.options)
        elif options is not None:
            self.__populate(options)

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
