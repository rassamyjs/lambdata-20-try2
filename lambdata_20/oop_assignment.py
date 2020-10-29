"""
OOP assignment for module 2:
    Create a basic class
    Clean up yesterday's code
    Make sure it can be read and understood by anyone

"""
# Important Notes
"""
Self will be put in to describe your class. In this instance, 
    self will mean Store
"""
import pandas as pd
import numpy as np

class Store:
    def __init__(self, name, storetype, isles, sqft, location):
        """
        Name of store
        Type of store this,
        How many isles is inside the store,
        How large it is,
        Where it is located 
        """
        self.name = str(name)
        self.type = str(storetype)
        self.isles = int(isles)
        self.sqft = float(sqft)
        self.location = str(location)
    
    def large_store(self):
        """
        Defining how large a store is based on square footage
        """
        return self.sqft > 1000

class Person():
    """
    Creating a person with parameters:
    person's name
    person's age
    person's bloodtype
    person's haircolor
    """
  def __init__(self, name, age, bloodtype, haircolor):
    self.name = str(name)
    self.age = int(age)
    self.bloodtype = str(bloodtype)
    self.haircolor = str(haircolor)


  def birthday(self):
    """
    Increases age by 1
    """
    return self.age + 1

  def hairchange(self, color):
    """
    changes the hair color
    """
    return str(color)


if __name__ == '__main__':

# This condition will only hold true if the module is ran (python oop_example.py) and not imported
    store1 = Store('BestBuy', 'Electronics', 15, 45700, 'In the Mountains')
    store2 = Store('Fake', 'Groceries', 7, 2000, 'Park City')   

    print('name: {} is a large store: {} and has: {} isles.'.format(store1.name, store1.large_store(), store1.isles))

    name = Person('Justin', 17, 'o', 'black')
    name1 = Person('Joe', 25, 'b', 'blond')
    
    print('Hello, {}! my name is {}, nice to meet you!'.format(name.name, name1.name))
    print("Today's birthday is {}! he is turning {}.".format(name.name, name.birthday()))
    print("{}'s hair is the color {}. He wants to dye it to match {}'s hair. {}'s hair is now {}.".format(name.name, name.haircolor, name1.name, name.name, name.hairchange('blond')))
  


