# Example of "continue"
def findNumbersModX(x, n):
    """
    Parameters: x -> int: x > 0
                n -> int: n > 0
    Print whether each number between 1 and n is divisible by x
    Returns: N/A
    """
    for i in range(1, n):
        if(i % x == 0):
            print(f"{i} is divisible by {x}")
            continue
        print(f"    {i} isn't divisible by {x}")


# Example of "break"
def findFactorsOrPrime(n):
    """
    Parameters: n -> int: n > 2
    Print whether each number between 2 and n has a factor, or if it
        is a prime number
    Returns: N/A
    """
    for i in range(2, n):
        for j in range(2, i):
            if(i % j == 0):
                factor = i//j
                print(f"{i} = {j} * {factor}")
                break
        else:
            print(f"    {i} is a prime number")


################################################################################


"""
TODO: Write a function that follows the criteria listed below
    The purpose of this function is to loop over integers, 1 to n, and print
    the xth factor, if it exists, or a message if it doesn't exist
        * Function should take in a parameter n, where n > 0
        * Function should take in a parameter x, where x > 0
        * Function should print the following message if the xth factor exists
            for each number between 1 and n
            "The xth factor of y is z"
        * Numbers that don't have have an xth factor should print the following
            message
            "y does not have an xth factor"
    Examples:
        "The 1st factor of 2 is 1"
        "The 2nd factor of 15 is 3"
        "1 does not have a 2nd factor"
        "6 does not have a 5th factor"
"""