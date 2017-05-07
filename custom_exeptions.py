class WrongClassException(Exception):
    def __init__(self, message):
        super().__init__(message)


class OverFlow(Exception):
    def __init__(self, message):
        super().__init__(message)
