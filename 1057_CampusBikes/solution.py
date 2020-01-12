import heapq
class Solution:
    def campus_bike(self, workers, bikes):
        def dist_fn(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        global_heap = []
        worker_heap = []

        for i in range(len(workers)):
            local_heap = []
            for j in range(len(bikes)):
                heapq.heappush(local_heap, (dist_fn(workers[i], bikes[j]), i, j))
            heapq.heappush(global_heap, heapq.heappop(local_heap))
            worker_heap.append(local_heap)
        
        res = [-1] * len(workers)
        used = set()
        num = 0
        while num != len(res):
            _, worker_idx, bike_idx = heapq.heappop(global_heap)
            while bike_idx in used:
                heapq.heappush(global_heap, heapq.heappop(worker_heap[worker_idx]))
                _, worker_idx, bike_idx = heapq.heappop(global_heap)
            res[worker_idx] = bike_idx
            used.add(bike_idx)
            num += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    # workers = [[0,0],[2,1]]
    # bikes = [[1,2],[3,3]]
    workers = [[0,0],[1,1],[2,0]]
    bikes = [[1,0],[2,2],[2,1]]
    print(sol.campus_bike(workers, bikes))



