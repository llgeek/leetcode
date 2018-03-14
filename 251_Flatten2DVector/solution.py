class Solution(object):
    def __init__(self, vectors):
        self.vectors = vectors
        self.rowid = 0
        self.colid = -1


    def next(self):
        self.colid += 1
        return self.vectors[self.rowid][self.colid]

    def hasNext(self):
        while self.rowid < len(self.vectors) and self.colid + 1 >= len(self.vectors[self.rowid]):
            self.rowid += 1
            self.colid = -1
        return True if self.rowid < len(self.vectors) else False
        
            
vectors = [
    [],
    [1,2],
    [3],
    [],
    [4,5,6]
]
s = Solution(vectors)
while s.hasNext():
    print(s.next())

