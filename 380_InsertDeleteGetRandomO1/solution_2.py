import random
class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.val2idx = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.val2idx:
            self.val2idx[val] = len(self.values)
            self.values.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val2idx:
            return False
        lastval = self.values[-1]
        self.val2idx[lastval] = self.val2idx[val]
        self.values[self.val2idx[val]] = lastval
        self.values.pop()
        self.val2idx.pop(val, 0)
        return True
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
