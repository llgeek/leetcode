"""
binary search

O(NlogM), where M is the length of search space
"""
import math
class Solution:
    def minmaxGasDist(self, stations, K):
        def possible(dis):
            return sum(int(math.ceil((p-q)/dis))-1 for p, q in zip(stations[1:], stations[:-1])) <= K

        lo, hi = 0, max(p-q for p, q in zip(stations[1:], stations[:-1]))
        while lo < hi - 10**-6:
            mid = (lo + hi) / 2
            if possible(mid):
                hi = mid
            else:
                lo = mid

        return lo

# import math
# class Solution(object):
#     def minmaxGasDist(self, stations, K):
#         """
#         :type stations: List[int]
#         :type K: int
#         :rtype: float
#         """
#         stations.sort()
#         step = 1e-9
#         left, right = 0, 1e9
#         while left <= right:
#             mid = (left + right) / 2
#             if self.isValid(mid, stations, K):
#                 right = mid - step
#             else:
#                 left = mid + step
#         return mid

#     def isValid(self, gap, stations, K):
#         for x in range(len(stations) - 1):
#             dist = stations[x + 1] - stations[x]
#             K -= int(math.ceil(dist / gap)) - 1
#         return K >= 0

if __name__ == "__main__":
    # stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # K = 9
    stations = [10, 19, 25, 27, 56, 63, 70, 87, 96, 97]
    K = 3
    sol = Solution()
    print(sol.minmaxGasDist(stations, K))
