class LenghtInputError(Exception):
    """Raise when input is not equal requirement lenght"""
    pass

class NotMenuError(Exception):
    """Raise when input is not contain letter or digit pointing on menu item"""
    pass

class WrongInput(Exception):
    """Raise when input is not equal requirements for current menu"""
    pass