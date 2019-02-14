class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        i = len(A)-1
        while i > 1:
            if A[i] < A[i-1] + A[i-2]:
                return A[i] + A[i-1] + A[i-2]
            i -= 1
        return 0

if __name__ == "__main__":
    # A = [3,2,3,4]
    A = [3,6,2,3]
    sol = Solution()
    print(sol.largestPerimeter(A))