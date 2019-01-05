import heapq
class Solution():
    def charitiableGiving(self, values):
        """
        type values: list of int
        rtype: list of 'A', 'B', 'C'
        """
        if len(values) <= 3:
            return ['A', 'B', 'C'][:len(values)] 
        gives = []
        heapq.heappush(gives, (values[0], 0))
        heapq.heappush(gives, (values[1], 1))
        heapq.heappush(gives, (values[2], 2))
        res = ['A', 'B', 'C']
        for val in values[3:]:
            top = heapq.heappop(gives)
            heapq.heappush(gives, (top[0] + val, top[1]))
            res.append(chr(ord('A') + top[1]))
        return res 
    

if __name__ == '__main__':
    values = [25, 8, 2, 35, 15, 120, 55, 42]
    print(Solution().charitiableGiving(values))

                
