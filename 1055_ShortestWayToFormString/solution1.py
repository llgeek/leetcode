"""
optimize to use pre-calculate index to speed up

"""
import bisect
class Solution:
    def shortest_way(self, source, target):    
        # if set(source) != set(target) or not source:
            # return -1

        indexes = [[] for _ in range(26)]
        for i, c in enumerate(source):
            indexes[ord(c) - ord('a')].append(i)
        
        res = 0
        i, j = -1, 0
        while j < len(target):
            if not indexes[ord(target[j]) - ord('a')]:
                return -1
            hi = bisect.bisect_left(indexes[ord(target[j]) - ord('a')], i)
            if hi == len(indexes[ord(target[j]) - ord('a')]):
                res += 1
                i = -1
            else:
                i = indexes[ord(target[j]) - ord('a')][hi]
                j += 1
        return res + (i != -1)

if __name__ == "__main__":
    sol = Solution()
    source = "abc"
    target = "abcbc"
    # source = "abc"
    # target = "acdbc"
    source = "xyz"
    target = "xzyxz"
    print(sol.shortest_way(source, target))