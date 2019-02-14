# 2nd attempt
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = Counter(tasks).most_common()
        maxtasklen = cnt[0][1]
        maxtasknum = 0
        for item in cnt:
            if item[1] == maxtasklen:
                maxtasknum += 1
            else:
                break
        return max(len(tasks), (n+1)*(maxtasklen-1) + maxtasknum)

if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(Solution().leastInterval(tasks, n))

