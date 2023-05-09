class InputException(Exception):
    def __init__(self, message: str = "Enter the Correct Input"):
        self.message = message
        super().__init__(self.message)
