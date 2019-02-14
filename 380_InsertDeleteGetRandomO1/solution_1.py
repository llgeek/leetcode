"""
second trial
"""

import random
class RandomizedSet(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.existval = dict()
        self.rnd = random


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.existval:
            self.array.append(val)
            self.existval[val] = len(self.array)-1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.existval:
            return False
        idx = self.existval[val]
        self.existval[self.array[-1]] = idx
        self.array[idx] = self.array[-1]
        self.array.pop()
        self.existval.pop(val)
        return True

        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.array[self.rnd.randint(0, len(self.array)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
