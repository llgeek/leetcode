"""
third trial
"""

from collections import Counter
class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        cnt = Counter(tasks).most_common()
        maxnum, maxcnt = 0, cnt[0][1]
        for pair in cnt:
            if pair[1] != maxcnt:
                break
            maxnum += 1
        return max(len(tasks), (cnt[0][1]-1) * (n+1) + maxnum)

if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    sol = Solution()
    print(sol.leastInterval(tasks, n))
