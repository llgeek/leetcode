

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = (1<<31)-1
        flag = 1 if x > 0 else -1
        x *= flag
        rev = 0
        while x:
            pop = x % 10
            x = x // 10
            if rev > INT_MAX // 10 or (rev == INT_MAX//10 and (pop > 7 if flag == 1 else pop > 8)): return 0
            rev = rev * 10 + pop
        return rev*flag

if __name__ == "__main__":
    # x = 1463847412
    # x = -8463847412
    x = -900000
    sol = Solution()
    print(sol.reverse(x))
