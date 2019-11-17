import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = []
        self.have = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.have:
          self.have[val] = len(self.val)
          self.val.append(val)
          return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.have:
          idx = self.have[val]
          self.val[-1], self.val[idx] = self.val[idx], self.val[-1]
          self.val.pop()
          self.have.pop(val)
          if idx < len(self.val):
            self.have[self.val[idx]] = idx
          return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.val)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()