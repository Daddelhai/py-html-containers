from .elements import Meta, Title, Head, Body

class Document:
    def __init__(self, title: str|None = None, lang: str = "en", charset: str = "utf-8"):
        self.lang = lang

        self.head = Head()

        if title is not None:
            self.head.add_child( Title(text=title) )
        self.head.add_child( Meta(attributes={"charset":charset}) )

        self.body = Body()


    def __str__(self):
        return f'<!DOCTYPE html><html lang="{self.lang}">'+str(self.head)+str(self.body)+'</html>'
