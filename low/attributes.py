from .base import ListBase


class HTMLAttribute:
    def __init__(self, name, value=True):
        self.name = name
        self.value = value

    def __str__(self):
        if isinstance(self.value, bool):
            return f'{self.name}'
        else:
            return f'{self.name}="{self.value}"'


class HTMLClassAttribute(HTMLAttribute, ListBase[str]):
    def __init__(self, values=None):
        super().__init__("class")
        self._data = values if values is not None else list[str]()

    def __str__(self):
        self.value = ' '.join(self._data)
        return super().__str__()
