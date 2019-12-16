public class Solution extends Reader4 

class Solution(Reader4):
    def __init__():

    def read(self, buf, n):
        readnum = 0
        buff4 = [None] * 4
        reachend = False
        while readnum < n and not reachend:
            readsize = read4(buff4)
            if readsize < 4:
                reachend = True
            for i in range(readsize):
                buf[readnum] = readsize[i]
                readnum += 1
                if readnum == n:
                    break
        return readnum