"""
utilize the property that hour and mins in watch is exponatial of 2
bit operation
"""

class Solution:
    def readBinaryWatch(self, num):
        return ['{:d}:{:02d}'.format(hour, mins) for hour in range(12) for mins in range(60)
            if (bin(hour) + bin(mins)).count('1') == num]

s = Solution()
print(s.readBinaryWatch(2))
