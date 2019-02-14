class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(tasks).most_common()
        ret = (n+1)*(cnt[0][1]-1)+1
        for pair in cnt[1:]:
            if pair[1] == cnt[0][1]:
                ret += 1
            else:
                break
        return max(ret, len(tasks))


if __name__ == "__main__":
    pass

        