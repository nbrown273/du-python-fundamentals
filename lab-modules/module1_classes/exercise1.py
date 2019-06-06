class MyTestClass():
    class_var = 'this is a class variable'
    _other_var = 'the leading underscore on this one tells the users they probably shouln\'t mess with it'

    def my_class_func():
        pass  # do stuff here

    def my_other_func():
        pass  # do more stuff here

#############################

# TODO: Define a class - "Car"
# TODO: The Car should have variables to represent the make and model, accepted as inputs. (the __init__ method)
# TODO: Define a function in the Car class "honk". This function should print something like "Honk!" to stdout


# testing
myCar = Car(make='Ford', model='Pinto')
myCar.honk()