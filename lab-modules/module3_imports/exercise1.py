# imports are needed when you want to use code that is not defined in the standard library (The standard library is loaded by default when Python is executed, such as "print")

# for example, this code needs to read data from a csv file. To accomplish this it needs the "csv" module, which has utilities for reading and writing csv files
import csv

file = open('eggs.csv', newline='')
spamreader = csv.reader(file, delimiter=',', quotechar='"')
for row in spamreader:
    print(', '.join(row))
file.close()


###########################
# the above import will import EVERYTHING in the named modules, however you can also import only specific things from a module if desired
from csv import reader # this imports only the "reader" object from the csv module


# you can also import your own classes and functions from your other files with the below syntax
# syntax: from <module> import <object names>
from hello import say_hello

say_hello()

###########################

# TODO: import the Artist class from your "main.py" file here
# TODO: create an artist object and print it's name to the console
