class ReadabilityError(Exception):
    """
    Base Class for lisibilite error
    """
    pass


class BadInputError(ReadabilityError):
    """
    Bad input errors
    """
    pass


class IOError(ReadabilityError):
    """
    Input Output errors
    """
    pass

class ArgumentParsingError(ReadabilityError):
    """
    Error occuring while parsing arguments
    """
    pass
