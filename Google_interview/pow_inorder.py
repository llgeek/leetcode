"""
implement 2^i*5^j
print numbers in order, without any input
stop output when use interrupt the program
"""

import time
import heapq

class Solution:
    def pow_inorder(self):
        """
        2^i*5^j
        print numebrs in accessdending order 
        """
        priq = [(1, 0, 0)]
        heapq.heapify(priq)
        valueset = set((1,0,0))
        while True:
            smallval, i, j = heapq.heappop(priq)
            valueset.discard((smallval, i, j))
            print(smallval)
            if (smallval * 2, i+1, j) not in valueset:
                heapq.heappush(priq, (smallval*2, i+1, j))
                valueset.add((smallval*2, i+1, j))
            if (smallval * 5, i, j+1) not in valueset:
                heapq.heappush(priq, (smallval*5, i, j+1))
                valueset.add((smallval*5, i, j+1))
            time.sleep(0.5)

s = Solution()
s.pow_inorder()



# numbers = [1]
# next_2 = 0
# next_5 = 0

# for i in range(100):
#     mult_2 = numbers[next_2]*2
#     mult_5 = numbers[next_5]*5

#     if mult_2 < mult_5:
#         next = mult_2
#         next_2 += 1
#     else:
#         next = mult_5
#         next_5 += 1

#      # The comparison here is to avoid appending duplicates
#     if next > numbers[-1]:
#         numbers.append(next)

# print (numbers)
