class Solution:
    def strobogrammaticNumber(self, num):
        strobogram = {'1': '1', '6': '9', '8': '8', '9': '6', '0':'0'}
        numstr = str(num)
        i, j = 0, len(numstr)
        while i <= j:
            if num[i] in strobogram and num[j] in strobogram and strobogram[num[i]] == num[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
