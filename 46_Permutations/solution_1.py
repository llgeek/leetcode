class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtracker(restnums, path):
            if not restnums:
                self.res.append(path[:])
                return
            else:
                for i in range(len(restnums)):
                    backtracker(restnums[:i] + restnums[i+1:], path + [restnums[i]])
        backtracker(nums, [])
        return self.res
