"""
second trial

"""
# class Node:
#     def __init__(self, val, isend):
#         self.val = val
#         self.next = {}
#         self.isend = isend

# class Trie:
#     def __init__(self):
#         self.root = {}
    
#     def addWord(self, word):
#         i = 0
#         curnode = self.root
#         while i < len(word):
#             if word[i] not in curnode:
#                 curnode[word[i]] = Node(word[i])
#             curnode = curnode[word[i]]
#             if i == len(word)-1:
#                 curnode.isend = True
    
#     def searchWord(self, word):
#         def helper(node, word, idx):
#             if idx == len(word)-1 
#             if word[i] == '.'

#         i = 0
#         curnode = self.root
#         while i < len(word):
#             if word[i] != '.' and word[i] not in curnode:
#                 return False
#             if word[i] == '.':
#                 return helper(curnode, word, i)
#         return curnode.isend


class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.trie = Trie()
        self.root = {}

        

    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        # self.trie.addWord(word)
        i = 0
        curnode = self.root
        while i < len(word):
            if word[i] not in curnode:
                curnode[word[i]] = {}
            curnode = curnode[word[i]]
            if i == len(word)-1:
                curnode['END'] = True
            i += 1


        

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(curnode, word, idx):
            if idx == len(word):
                return curnode.get('END', False)
            if word[idx] != '.':
                if word[idx] not in curnode:
                    return False
                else:
                    curnode = curnode[word[idx]]
                    idx += 1
                    return helper(curnode, word, idx)
            else:
                return any(helper(curnode[c], word, idx+1) for c in curnode.keys() if c in 'abcdefghijklmnopqrstuvwxyz')

        return helper(self.root, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    obj = WordDictionary()
    word = 'bad'
    obj.addWord(word)
    param_2 = obj.search(word)
