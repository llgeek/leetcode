import random
class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.index = {}

    
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            return False
        else:
            self.values.append(val)
            self.index[val] = len(self.values)-1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        else:
            self.values[self.index[val]] = self.values[-1]
            self.index[self.values[-1]] = self.index[val]
            self.values.pop()
            self.index.pop(val, 0)
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.values[random.randrange(0, len(self.values))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

