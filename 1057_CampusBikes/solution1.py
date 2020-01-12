"""
pigeonhole sorting when dist(worker, bike) is bounded
"""

class Solution:
    def campus_bike(self, workers, bikes):
        def dist_fn(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        distances = [[] for _ in range(2001)]   # distance is bounded by 2000
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distances[dist_fn(workers[i], bikes[j])].append((i, j))
        res = [None] * len(workers)
        used = set()
        for distance in distances:
            for w_id, b_id in distance:
                if res[w_id] is None and b_id not in used:
                    res[w_id] = b_id
                    used.add(b_id)
        return res

if __name__ == "__main__":
    sol = Solution()
    workers = [[0,0],[2,1]]
    bikes = [[1,2],[3,3]]
    # workers = [[0,0],[1,1],[2,0]]
    # bikes = [[1,0],[2,2],[2,1]]
    print(sol.campus_bike(workers, bikes))



