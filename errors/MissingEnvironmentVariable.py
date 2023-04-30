class MissingEnvironmentVariableError(Exception):
    def __init__(self, variable: str):
        self.variable = variable
        super().__init__()

    def __str__(self):
        return f'Environment variable {self.variable} not found.'
