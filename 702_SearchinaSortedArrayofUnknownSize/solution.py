# class ArrayReader:
#     def get(k):
#         return idx

class Solution:
    def search(self, reader, target):
        def find_rightbound(reader, target):
            right = 1
            while reader.get(right) < target:
                right <<= 1
            return right
        
        left, right = 0, find_rightbound(reader, target)
        while left <= right:
            mid = (left + right) // 2
            kval = reader.get(mid)
            if kval < target:
                left = mid + 1
            elif kval > target:
                right = mid - 1
            else:
                return mid
        return -1

        
            