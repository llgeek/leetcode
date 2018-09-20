class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        if k == 0:
            from collections import Counter
            cnt = Counter(nums)
            return len([key for key, num in cnt.items() if num > 1])
        res = 0
        numset = set(nums)
        while numset:
            num = numset.pop()
            tmpnum = num
            while tmpnum + k in numset:
                res += 1
                tmpnum = tmpnum + k
                numset.discard(tmpnum)
            tmpnum = num
            while tmpnum - k in numset:
                res += 1
                tmpnum -= k
                numset.discard(tmpnum)
        return res

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    k = -1
    
    print(Solution().findPairs(nums, k))
