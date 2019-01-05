class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

class HuffmanTree():
    def __init__(self):
        self.root = TreeNode()

    def addChar(self, code):
        curnode = self.root
        char, encodnum = code.split('\t')
        if char == '[newline]':
            char = '\n'
        for n in encodnum:
            if n == '0':
                if not curnode.left:
                    curnode.left = TreeNode()
                curnode = curnode.left
            elif n == '1':
                if not curnode.right:
                    curnode.right = TreeNode()
                curnode = curnode.right
        curnode.val = char
    
    def decodeStr(self, encodstr):
        res = []
        curnode = self.root
        for num in encodstr:
            if num == '1':
                curnode = curnode.right
            else:
                curnode = curnode.left
            if curnode.val:
                res.append(curnode.val)
                curnode = self.root
        return ''.join(res)
        


class Solution():
    def buildHuffman(self, encodarray):
        self.huffmantree = HuffmanTree()
        for encod in encodarray:
            self.huffmantree.addChar(encod)

    def decode(self, encodstr):
        return self.huffmantree.decodeStr(encodstr)
    

def processTests(inputfile):
    encodarray = []
    sol = Solution()
    with open(inputfile, 'r') as rf:
        n = int(next(rf))
        for i in range(n):
            encodstr = next(rf)
            encodarray.append(encodstr)
        encodstr = next(rf)
    sol.buildHuffman(encodarray)
    return sol.decode(encodstr)

if __name__ == '__main__':
    inputfile = 'input.txt'
    print(processTests(inputfile))

        
