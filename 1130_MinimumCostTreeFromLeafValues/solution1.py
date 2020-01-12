"""
greedy solution
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            minidx = arr.index(min(arr))
            left = arr[minidx-1] if minidx > 0 else (1<<31) - 1
            right = arr[minidx+1] if minidx < len(arr) - 1 else (1<<31) - 1
            res += min(left, right) * arr[minidx]
            arr.pop(minidx)
        return res