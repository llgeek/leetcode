from typing import List
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks).most_common()
        mostcomnum, mostcomval = 0, cnt[0][1]
        for _, val in cnt:
            if val == mostcomval:
                mostcomnum += 1
            else:
                break
        return max(len(tasks), (n + 1) * (mostcomval-1) + mostcomnum)

        
