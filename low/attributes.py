
class HTMLAttribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        if self.value is None:
            return f"{self.name}"
        else:
            return f"{self.name}={self.value}"