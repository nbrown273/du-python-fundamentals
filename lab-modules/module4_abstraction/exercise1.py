# In programming, the principle of abstraction dictates that each distinct piece of functionality should be implemented in
# only one place in the source code. This helps avoid duplication of effort and keeps future changes managable.
# When you encounter similar functionality, any differences should be abstracted away so that a single functional unit 
# can be put in their place. This is also often referred to as DRY (Don't Repeat Yourself) design

# This is easy to state but has nuances in practice.

# Let's start with a high level example of abstraction, focusing on how it's used to your advantage.
# The builtin method open can be used to open files for many different purposes. Use the other builtin method, help, to 
# investigate some of the options.
help(open)

# Now, let's look at a more detailed example showing how abstraction is implemented.
# The standard library module 'inspect' can be used to look at the source code of other objects in python.
# Examine the source code of the 'csv' module.
import inspect
import csv
for line in inspect.getsourcelines(csv)[0]:
    print(line[:-1])
# Can you spot an example of one function serving multiple use cases? Which steps of the function are the result
# of abstracting away differences in the two use cases?

# You likely noticed that there's a lot of logic hidden inside the modules of the standard library that we don't need to think about.
# The pairing of state and behavior into functional units, often hiding details from the user, is known as encapsulation. 
# Both abstraction and encapsulation often go hand in hand. 

# TODO: Identify and abstract away a section of the main module that would be useful if abstracted into a separate method
# (the section may not be duplicated right now, but would likely be duplicated in the future).
# TODO: The main driver program can be thought of as two steps from a high level: loading data and analyzing its content.
# Split the main program into two separate methods based on this logical separation. 


