# Composition is when one class is used to create part of, or "compose", another class
class Car:

    def __init__(self, make, model, year, engine_cylinders, engine_volume, horsepower):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(engine_cylinders, engine_volume, horsepower)  # here we use the Engine class as a component of the Car class


class Engine:

    def __init__(self, cylinders, volume, horsepower):
        self.cylinders = cylinders
        self.volume = volume
        self.horsepower = horsepower

################################


# Inheritance is when one class inherits (and extends) the methods and variables of another class
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)

# even though inputSides() and dispSides() are not defined in the Triangle class, they can be used on Triangle objects
# since they were inherited from the Polygon class

################################

# TODO: Define two classes of your choosing
    # initialize at least three variables for each class
    # at least one of these variables should be an instance of the other class (composition)

# TODO: define a function in each of your classes
    # the function in the class that uses composition should utilize the method of the other class.
