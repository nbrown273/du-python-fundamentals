# List Comprehension Example 
def getListPowN(x, n):
    """
    Parmaeters: x -> int: x > 0
                n -> int: n >= 0
    Generate a list of integers, 1 to x, raised to a power n
    Returns: list(int)
    """
    return [i**n for i in range(1, x)]


# Dictionary Comprehension Example
def getDictComprehension(keys, vals):
    """
    Parameters: keys -> list(str)
                vals -> tuple(int)
    Generate a dictionary comprehension based on a list and tuple
    Returns: dict
    """
    return {key: val for key, val in zip(keys, vals)}


################################################################################


"""
TODO: Write a function that follows the criteria listed below
    The purpose of this function is to generate a dictionary object whose
    keys and values follow the criteria below:
        * Function should take in a parameter "letters", where "letters" is a
            list of strings of length 1
        * Function should take in a parameter "lengths", where "lengths" is a
            list of ints >= 0
        * The length of "letters" and "lengths" have to be equal
        * If the lengths of "letters" and "lengths" are not equal, return the
            an error message
    Example:
        letters=["a", "b", "c", "d"]
        lengths=[0, 1, 2, 3]
        returns {"a0": "", "b1": "b", "c2": "cc", "d3": "ddd"}
"""