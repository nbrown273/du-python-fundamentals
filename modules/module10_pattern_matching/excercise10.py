# Example without Regex
def matchWithoutRegex(password): 
    """
    Parameters: password -> str
    Loops a string through various filters to check if it is acceptable
    Returns: bool
    """
    if(not password.startswith("b")):
        return False
    if(password.count("a") < 2):
        return False
    return True


# Example with Regex
from re import match
def matchWithRegex(password):
    """
    Parameters: password -> str
    Determine if a password starts with 'a', has any character, followed by 'b'
    Returns: bool
    """
    if(match(pattern=r"a.b", string=password)):
        return True
    return False


################################################################################


"""
TODO: Write a function that follows the criteria listed below
    The purpose of this function is to validate whether a string meets the
    following parameters:
        * Function should take in a parameter "password", where "password"
            is a string
        * "password" should start with the letter "a"
        * "password" should end with the letter "z"
        * "password" should have at least 1 of the following letters:
            "d", "t", "c", "u", "p"
        * "password" should be at least 10 letters longs
        * "password" cannot contain any numbers, 0-9
    Examples:
        password="aditucquepz"
        Returns: True

        password="udpqmzgnau"
        Returns: False

        password="a1dtcuppbz"
        Returns: False
"""