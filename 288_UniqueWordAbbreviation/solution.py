class Solution:
    def __init__(self, dictionary):
        self.abbrset = dict()
        for word in dictionary:
            if len(word) <= 2:
                abbr = word
            else:
                abbr = word[0] + str(len(word)-2) + word[-1]
            if abbr in self.abbrset:
                self.abbrset[abbr].add(word)
            else:
                self.abbrset[abbr] = {word}
        
            
    def isUnique(self, word):
        abbr = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
        if abbr in self.abbrset and word in self.abbrset[abbr] and len(self.abbrset[abbr]) == 1:
            return True
        else:
            return False

dictionary = { "dear"}
s = Solution(dictionary)
print(s.isUnique('door'))
