class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curnode = self.root
        for w in word:
            if w not in curnode:
                curnode[w] = {}
            curnode = curnode[w]
        curnode['end'] = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(subword, curnode):
            if len(subword) == 1:
                if subword == '.':
                    for node in curnode.keys():
                        if 'end' in curnode[node]:
                            return True
                    return False
                else:
                    if subword not in curnode or 'end' not in curnode[subword]:
                        return False
                    else:
                        return True
                    
            if not subword:
                return False
            if subword[0] == '.':
                for node in curnode.keys():
                    if helper(subword[1:], curnode[node]):
                        return True
                return False
            else:
                if subword[0] not in curnode:
                    return False
                else:
                    return helper(subword[1:], curnode[subword[0]])
        curnode = self.root
        for i, c in enumerate(word):
            if c == '.':
                return helper(word[i:], curnode)
            else:
                if c not in curnode:
                    return False
                curnode = curnode[c]

        return 'end' in curnode 
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == '__main__':
    # obj = WordDictionary()
    # print(obj.addWord("bad"))
    # print(obj.addWord("dad"))
    # print(obj.addWord("mad"))
    # print(obj.search("pad"))
    # print(obj.search("bad"))
    # print(obj.search(".ad"))
    # print(obj.search("b.."))
    # print(obj.search('b'))
    # print(obj.search('...'))

    obj = WordDictionary()
    print(obj.addWord("a"))
    print(obj.addWord("a"))
    print(obj.search("."))
    print(obj.search("a"))

    print(obj.search("aa"))
    print(obj.search("a"))
    print(obj.search(".a"))
    print(obj.search('a.'))
    # print(obj.search('...'))
