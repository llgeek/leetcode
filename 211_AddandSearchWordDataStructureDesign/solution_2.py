class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for i in range(len(word)):
          if word[i] not in node:
            node[word[i]] = {}
          node = node[word[i]]
          if i == len(word)-1:
            node['END'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(node, idx):
          if idx == len(word):
            return node.get('END', False)
          if word[idx] == '.':
            return any(helper(node[c], idx+1) for c in node.keys() if c in 'abcdefghijklmnopqrstuvwxyz')
          else:
            if word[idx] not in node:
              return False
            else:
              return helper(node[word[idx]], idx + 1)

        return helper(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)