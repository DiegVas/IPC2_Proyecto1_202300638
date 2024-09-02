class ErrorManager:
    def __init__(self):
        self.errors = ""

    def add_error(self, error):
        if self.errors:
            self.errors += "\n"
        self.errors += error

    def has_errors(self):
        return bool(self.errors)

    def get_errors(self):
        return self.errors
