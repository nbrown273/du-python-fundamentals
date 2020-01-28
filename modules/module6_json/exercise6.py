from json import load


# Example of reading from JSON file
def loadJSON(fileName):
    """
    Parameters: fileName -> str
    Loads JSON data from a specified file
    Returns: dict / Error Message
    """
    try:
        with open(fileName, "r") as r:
            data = load(fp=r)
        return data
    except FileNotFoundError as err:
        return f"Error in loadJSON: { err }"


# Example of recursively finding all keys in a dict
def nestedKeys(dictObj, keys):
    # Loop through each key value
    for key, val in dictObj.items():
        keys.append(key)
        # Check for iterable
        if(type(val) is list or type(val) is tuple):
            for item in val:
                # Find nested keys
                if(type(item) is dict):
                    nestedKeys(dictObj=item, keys=keys)
        # Find nested keys
        if(type(val) is dict):
            nestedKeys(dictObj=val, keys=keys)


################################################################################


"""
TODO: Write a function that follows the criteria listed below
    The purpose of this function is to loop through list of page objects in the
    "wiki.json" file and find the count of given substrings on each page
        * Function should take in a parameter "substrings", where substring
            is a list of strings
        * Function should return a dict object, mapping the page titles
            to a dict, mapping the given substrings counts on the page
    Example
        * Inputs: substrings=["a", "b"]
        * Returns: {'Pear': {'a': 1394, 'b': 232},
                    'Apple': {'a': 4239, 'b': 848},
                    'Banana': {'a': 8626, 'b': 1671},
                    'Pumpkin': {'a': 2094, 'b': 415},
                    'Pitaya': {'a': 923, 'b': 148}}
"""
