
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curnode = self.root
        for c in word:
            if c not in curnode:
                curnode[c] = {}
            curnode = curnode[c]
        curnode['end'] = True
            

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curnode = self.root
        for c in word:
            if c not in curnode:
                return False
            curnode = curnode[c]
        return 'end' in curnode

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curnode = self.root
        for c in prefix:
            if c not in curnode:
                return False
            curnode = curnode[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    obj = Trie()
    word = 'apple'
    obj.insert(word)
    print(obj.search('app'))
    print(obj.startsWith('app'))
    print(obj.search('apple'))
    print(obj.insert("app"))
    print(obj.search('app'))


