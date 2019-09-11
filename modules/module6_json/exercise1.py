# JavaScript Object Notation or JSON is a commonly used data interchange format.
# It is humean readable and easy to parse by a machine, while using a minimal set of characters 
# to explain a wide variety of structures. For these reasons, it is a very popular option when communicating with APIs.

# This example prints the JSON taken from an example Todo application. 
# It also shows how to read (load/loads) and write (dump/dumps) a JSON string using the 'json' python module.
from urllib.request import urlopen
import json
example_url = 'https://jsonplaceholder.typicode.com/todos'
with urlopen(example_url) as response:
   data = json.load(response)
   print(json.dumps(data, indent=4))

# Now it's your turn
# TODO: Print the user id of todo id=12 and print the title of the todo with id=50
# Note: you can call the url 'https://jsonplaceholder.typicode.com/todos/<my-id>' to get just the todo with id=<my-id>
from urllib.request import urlopen
import json
base_url = 'https://jsonplaceholder.typicode.com/todos/{}'
with urlopen(example_url.format()) as response: # insert the id as needed
   data = None # call the appropriate json method to get a dictionary representing the todo
   print(data) # access the correct element to print what's desired
# repeat for the other id and desired element

# TODO: BONUS - can you abstract away the differences for the two requests?

# Finally, before updating the music project, let's take a look at how the json module was used to generate your JSON file source.
# TODO: Inspect the code in generation/json_generator.py to find where the json module is used. 
# How is this different from the first example of using json.dumps above?

# TODO: Write a completely new load function, that creates a list of Artist objects from the JSON file "data/faked/store.json"
