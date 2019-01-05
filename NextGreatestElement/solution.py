from collections import deque
class Solution():
    def next_greatest_element(self, array):
        if not array:
            return []
        res = [-1 for _ in range(len(array))]
        stack = deque()
        stack.append((array[0], 0))
        for i in range(1, len(array)):
            if not stack:
                stack.append((array[i], i))
                continue
            while stack and stack[-1][0] < array[i]:
                val, idx = stack.pop()
                res[idx] = array[i]
            stack.append((array[i], i))
        return res 


if __name__ == '__main__':
    # array = [6, 2, 34, -56, 8, 42, 1]
    array = [11,13,21,3]
    print(Solution().next_greatest_element(array))
            
            
