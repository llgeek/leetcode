class Solution:
    READPOS = 0
    WRITEPOS = 0
    BUFF4 = [""] * 4
    def readNChar(self, buf, n):
        def read4(buf):
            """
            read 4 characters at a time from buf
            
            return number of characters it read
            """
            return 0
        for i in range(n):
            if self.READPOS < self.WRITEPOS:
                buf[i] = self.BUFF4[self.READPOS]
                self.READPOS += 1
            else:
                self.READPOS = 0
                self.WRITEPOS = read4(self.BUFF4)
                if self.WRITEPOS == 0:
                    return i
        return n