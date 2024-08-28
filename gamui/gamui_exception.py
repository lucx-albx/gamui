"""
This file it's used by the gamui module for raise custom error, in this way the different
error that we can see gonna be more easy to fix it and understand it.
"""
class GeneralError(Exception):
    def __init__(self, message : str) -> None:
        self.set_message(message)
        super().__init__(self.get_message())

    def set_message(self, msg : str) -> None:
        self.__message = msg

    def get_message(self) -> str:
        return self.__message
    
class ConstraintHeightError(GeneralError):
    def __init__(self, message : str) -> None:
        super().set_message(message)
        super().__init__(super().get_message())

class ConstraintWidthError(GeneralError):
    def __init__(self, message : str) -> None:
        super().set_message(message)
        super().__init__(super().get_message())

class ConstraintAxiesXError(GeneralError):
    def __init__(self, message : str) -> None:
        super().set_message(message)
        super().__init__(super().get_message())

class ConstraintAxiesYError(GeneralError):
    def __init__(self, message : str) -> None:
        super().set_message(message)
        super().__init__(super().get_message())

class NegativeNumberError(GeneralError):
    def __init__(self, message : str) -> None:
        super().set_message(message)
        super().__init__(super().get_message())
