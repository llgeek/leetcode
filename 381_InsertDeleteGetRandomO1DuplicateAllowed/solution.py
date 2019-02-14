import random
class RandomizedCollection:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []    # val: index in index dict's list
        self.index = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            self.values.append((val, len(self.index[val])))
            self.index[val].append(len(self.values)-1)
            return False
        else:
            self.values.append((val, 0))
            self.index[val] = [len(self.values)-1]
            return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            lastval, crtidx = self.values[-1]
            rmidx = self.index[val][-1]
            self.values[rmidx] = (lastval, crtidx)
            self.index[lastval][crtidx] = self.index[val][-1]
            self.values.pop()
            self.index[val].pop()
            if not self.index[val]:
                self.index.pop(val, 0)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.values[random.randrange(0, len(self.values))][0]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
