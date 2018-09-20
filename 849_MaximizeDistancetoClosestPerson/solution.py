class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        heap = []
        s = 0
        maxdist, sid = 0, 0
        for i, v in enumerate(seats):
            if not v and i - s + 1 > maxdist:
                maxdist = i - s + 1
                sid = i
            elif v:
                s = i
        s = 0
        for i, v in enumerate(seats[::-1]):
            if not v and i - s + 1 > maxdist:
                maxdist = i - s + 1
                sid = i
            elif v:
                s = i
        return sid

if __name__ == '__main__':
    seats = [1, 0, 0, 0, 1, 0, 1]
    print(Solution().maxDistToClosest(seats))