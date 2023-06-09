class InvalidParserFactoryOption(Exception):
    def __init__(self, value, message="Value is not a valid parse option"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'


class MultipleValuesParserFactoryClass(Exception):
    def __init__(self, value, message="Multiple values are not valid"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'
