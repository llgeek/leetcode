class Solution:
    def divideChocolate(self, sweetness, k):
        def valid(target):
            acc, cnt = 0, 0
            for sweet in sweetness:
                acc += sweet
                if acc >= target:
                    acc = 0
                    cnt += 1
            return cnt >= k + 1

        left, right = min(sweetness), sum(sweetness)
        while left < right:
            mid = left + (right - left) // 2
            if valid(mid):
                left = mid + 1
            else:
                right = mid
        return right - 1


if __name__ == "__main__":
    sol = Solution()
    # nums = [1,2,3,4,5,6,7,8,9]
    # m = 5
    # nums = [5,6,7,8,9,1,2,3,4]
    # m = 8
    nums = [1,2,2,1,2,2,1,2,2]
    m = 2
    print(sol.divideChocolate(nums, m))


