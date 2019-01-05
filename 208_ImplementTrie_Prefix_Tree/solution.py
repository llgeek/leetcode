class Node:
    def __init__(self, val):
        self.val = val
        self.children = set()
        self.isend = False

class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return
        curnode = self.root
        for c in word[:-1]:
            ifexist = False
            for child in curnode.children:
                if c == child.val:
                    ifexist = True
                    curnode = child
                    break
            if not ifexist:
                newnode = Node(c)
                curnode.children.add(newnode)
                curnode = newnode
        for child in curnode.children:
            if word[-1] == child.val:
                child.isend = True
                return
        newnode = Node(word[-1])
        newnode.isend = True
        curnode.children.add(newnode)
        return
                                
                
                    
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        curnode = self.root
        for c in word[:-1]:
            ifexist = False
            for child in curnode.children:
                if c == child.val:
                    curnode = child
                    ifexist = True
                    break
            if not ifexist: return False

        for child in curnode.children:
            if word[-1] == child.val and child.isend:
                return True
        return False
        

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curnode = self.root
        for c in prefix:
            ifexist = False
            for child in curnode.children:
                if c == child.val:
                    ifexist = True
                    curnode = child
                    break
            if not ifexist: return False
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
