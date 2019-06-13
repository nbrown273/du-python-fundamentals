# There are six new pieces of syntax that, when taken together, summarize 
# most of the options for exception handling in python. The broadly have to do with either:
#  1) Raising exceptions
#  2) Responding to exceptions

# When an exception is raised, the current execution block is stopped and the exception is passed to the block's caller.
# If that block does not respond to the exception, the previous step repeats until something handles the exception
# or the entire program is exited.
import random
def problem_source():
    if random.randint(0,1):
        raise Exception("A random exception was raised.")
    print("Phew. Save for now.")
while True:
    problem_source()

# Often exceptions are raised on purpose when an assumption or requirement about the inputs or output of a method is not satisfied.
# There is a shorthand for asserting something is true and causing an exception if it's false.
assert (2 + 2 == 4), "Two plus two is four" # should pass silently
assert ("I" in "TEAM"), "I should be in TEAM" # should fail 

# TODO: Add your own assertion to the load method (or a helper function) to ensure at least one artist is loaded.

# The other side of error handling is responding to exceptions. Take a look at the very contrived example below:
import random
def contrived_example():
    try:
        print("I'm trying something...")
        x = random.randint(0, int(input("Enter the max roll: ")))
        print(f"...rolled a {x}")
        assert (x > 5), "That was unlucky"
    except AssertionError as ex:
        print("When we fail...")
        print(ex)
    except Exception as ex:
        print("THAT was unexpected")
        print(ex)
    else:
        print("When we succeed...")
        print("That was lucky")
    finally:
        print("Wrapping up")
        print("We can always try again")

while input("\nTake your chances (y/n)? ") == 'y':
    contrived_example()

#In the example there are four key words: try, except, else, finally. Can you figure out when each block is triggered? 
# What is each block likely used for based on when it's triggered?
# TODO: Divide the roll by another random integer that's possibly zero. 
# TODO: Catch the new possible exception and print out your own message.

# TODO: Add exception handling to your load script that will be triggered if any of the csv files cannot be found. Test it
# out by moving one of the files and running main.


