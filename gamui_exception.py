"""
Module used for raise custom error for the gamui module.
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