import django.middleware.csrf as csrf
from .elements import Input

class DjangoCSRFToken(Input):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attr.name = "csrfmiddlewaretoken"
        self.attr.value = csrf.get_token(request)
        self.attr.type = "hidden"