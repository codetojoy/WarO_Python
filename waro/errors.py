
class ConfigurationError(Exception):
    """Exception raised for errors re: configuration file."""

    def __init__(self, message="unknown configuration error"):
        self.message = message
        super().__init__(self.message)
