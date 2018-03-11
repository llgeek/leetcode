"""
use idea of combination
"""
class Solution:
    def readBinaryWatch(self, num):
        hours = [1, 2, 4, 8]
        mins = [1,2,4,8,16,32]
        result = []
        for i in range(5):
            j = num - i
            hourchoice = self.generateCombinationSum(hours, i)
            minschoice = self.generateCombinationSum(mins, j)
            for h in hourchoice:
                if h > 11: 
                    continue
                for m in minschoice:
                    if m > 59: 
                        continue
                    result.append("{:d}:{:02d}".format(h, m))
        return result


    def generateCombinationSum(self, numlist, count):
        def generateCombinationSumHelper(count, pos, tmpsum):
            if not count:
                result.append(tmpsum)
                return
            for i in range(pos, len(numlist)):
                generateCombinationSumHelper(count-1, i+1, tmpsum+numlist[i])

        result = []
        generateCombinationSumHelper(count, 0, 0)
        return result

s = Solution()
print(s.readBinaryWatch(2))