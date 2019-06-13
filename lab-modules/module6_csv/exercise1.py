# STOP HERE: If you have finished the json exercises within the first day of modules, 
# use this time to review the past content and aid your peers. 

# You've probably already heard of CSV files, but are you aware that there is no agreed upon standard
# for CSV file formats? As a result, it can be very helpful to have a csv module that encapsulates the
# same behavior for all the common CSV formats. It also allows custom CSV formats to be defined, and defines
# helpful utilities for converting between CSV and python dictionaries.

# The following code writes a series of dictionaries to a unix compatible csv file.
from csv import DictWriter
data = [
    {'name': 'Susana', 'media': 'song', 'attribute': 'lonely'},
    {'name': 'Arthur', 'media': 'lore', 'attribute': 'invincible'},
    {'name': 'Doug', 'media': 'toon', 'attribute': 'homely'}
]
with open('characters.csv', 'w', newline='') as fp:
    writer = DictWriter(fp, data[0].keys(), dialect='unix')
    writer.writeheader()
    writer.writerows(data)

# TODO: Change the code to produce an excel compatible, tab delimited file (.txt extension)

# TODO: Use the DictReader class to read the contents of the tab delimited file back in as a list of dictionaries.
# A template for the previous dialect is below
from csv import DictReader
with open('characters.csv') as file:
    reader = DictReader(file)
    for record in reader:
        print(record)
    
# TODO: Modify the load method to read in the all of the csv files in data/faked. Store lists of each type of
# object in a dictionary where the key is the name of the type. 
# The previously composed objects will now contain a list of objects ids instead. Can you figure out why this is beneficial?
# TODO: Modify the analysis and class methods as needed to support the cross referencing of ids in place of nested objects.





