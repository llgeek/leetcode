class Solution:
    remainSize = 0
    remainIdx = 0
    remainBuf = [""] * 4
    def readNChar(self, buf, n):
        def read4(buf):
            """
            read 4 characters at a time from buf
            
            return number of characters it read
            """
            return
            
        idx = 0
        while idx < n:
            while self.remainIdx < self.remainSize:
                buf[idx] = self.remainBuf[self.remainIdx]
                idx += 1
                self.remainIdx += 1
            if self.remainSize <= self.remainIdx:
                self.remainIdx = 0
                self.remainSize = read4(self.remainBuf)
            if self.remainSize == 0:
                break
        return idx

            

        
