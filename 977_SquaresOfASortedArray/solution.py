class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return []
        if A[0] >= 0:
            return list(map(lambda  x: x**2, A))
        if A[-1] < 0:
            return list(map(lambda x: x**2, A))[::-1]
        idx = 0
        while idx +1 < len(A) and A[idx+1] < 0:
            idx += 1
        left, right = idx, idx + 1
        res = []
        while left >= 0 and right < len(A):
            if -A[left] < A[right]:
                res.append(A[left]**2)
                left -= 1
            else:
                res.append(A[right]**2)
                right += 1
        while left >= 0:
            res.append(A[left]**2)
            left -= 1
        while right < len(A):
            res.append(A[right]**2)
            right += 1
        return res

if __name__ == "__main__":
    A = [-7, -3, 2, 3, 11]
    sol = Solution()
    print(sol.sortedSquares(A))
