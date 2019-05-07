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
