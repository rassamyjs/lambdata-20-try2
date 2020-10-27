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

if __name__ == '__main__':
# This condition will only hold true if the module is ran (python oop_example.py) and not imported
    store1 = Store('BestBuy', 'Electronics', 15, 45700, 'In the Mountains')
    store2 = Store('Fake', 'Groceries', 7, 2000, 'Park City')   

    print('name: {} is a large store: {} and has: {} isles.'.format(store1.name, store1.large_store(), store1.isles))