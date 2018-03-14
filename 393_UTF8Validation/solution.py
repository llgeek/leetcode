class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def check10seq(startidx, num, maxlen):
            if startidx >= maxlen or startidx + num > maxlen:
                return False
            while num:
                if data[startidx + num-1] & 0b11000000 != 0b10000000:
                    return False
                num -= 1
            return True
                    
        i = 0
        while i < len(data):
            if not (data[i] & 0b10000000):
                i += 1
            elif data[i] & 0b11100000 == 0b11000000:
                if not check10seq(i+1, 1, len(data)):
                    return False
                i += 2
            elif data[i] & 0b11110000 == 0b11100000:
                if not check10seq(i+1, 2, len(data)):
                    return False
                i += 3
            elif data[i] & 0b11111000 == 0b11110000:
                if not check10seq(i+1, 3, len(data)):
                    return False
                i += 4
            else:
                return False
        return True

print(Solution().validUtf8([197,130,1]))
