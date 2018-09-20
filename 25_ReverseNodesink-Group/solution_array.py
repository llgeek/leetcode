"""
simplify the problem

the input is a array, instead of an arraylist
"""

class Solution:
    def kReverse(self, array, k):
        """
        :type array: list of int
        :type k: int
        :rtype: list of int
        """
        stepsize = k - 1
        start = 0
        while start < len(array):
            if stepsize <= 0:
                stepsize = k - 1
                start += (stepsize) // 2 + 1
                if start + stepsize >= len(array):
                    break
            array[start], array[start + stepsize] = array[start+stepsize], array[start]
            start += 1
            stepsize -= 2

if __name__ == '__main__':
    array = [1,2,3,4,5,6, 7]
    k = 3
    Solution().kReverse(array, k)
    print(array)

