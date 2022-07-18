import django.middleware.csrf as csrf
from .elements import Input


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
    def __init__(self, value=None, max=None, min=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.type = "date"


class TimeInput(DateTimeInput):
    def __init__(self, value=None, max=None, min=None, *args, **kwargs):
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
