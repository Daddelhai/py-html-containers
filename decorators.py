from django.http import HttpResponse
import inspect
import asyncio
from lib.html.document  import Document


def HTMLDocument(title: str = None, lang: str = "en", charset: str = "utf-8"):
    def decorator(func):
        def wrapper(request):
            document = Document(title=title, lang=lang, charset=charset)

            if inspect.iscoroutinefunction(func):
                asyncio.run(func(request, document.head, document.body))
            else:
                func(request, document.head, document.body)
            return HttpResponse(str(document))
        return wrapper
    return decorator
