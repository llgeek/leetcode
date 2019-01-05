

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > 0 else -1
        x = abs(x)
        reverx = flag * int(str(x)[::-1])
        if reverx > 1<<31-1 or reverx < - 1<<31:
            return 0
        else:
            return reverx
    

if __name__ == "__main__":
    x = 1463847412
    sol = Solution()
    print(sol.reverse(x))
