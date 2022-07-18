from .elements import Form, Input, Textarea, Select, DjangoCSRFToken
from .low.base import HTMLContainerBase


class HTMLForm(HTMLContainerBase):

    def __init__(self, method="POST", action=None, **kwargs):
        if "attributes" in kwargs:
            kwargs["attributes"]["method"] = method.upper()
        else:
            kwargs["attributes"] = {
                "method": method.upper()
            }

        if action is not None:
            kwargs["attributes"]["action"] = action

        self._formAttr = kwargs

    def __str__(self):
        form = Form(**self._formAttr)

        for key, element in self.__dict__.items():
            if key.startswith("_"):
                continue

            if not isinstance(element, HTMLContainerBase):
                raise TypeError("invalid form element")

            element.attr.name = key
            form.add_child(element)

        if "csrfmiddlewaretoken" not in self.__dict__:
            form.add_child(DjangoCSRFToken())

        return str(form)
