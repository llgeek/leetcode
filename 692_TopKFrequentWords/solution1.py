from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = Counter(words)
        heap = []
        # heapq.heapify(heap)
        for key in cnt:
            heapq.heappush(heap, (-cnt[key], key))
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])

        return ret


if __name__ == '__main__':
    #words = ["i", "love", "leetcode", "i", "love", "coding"]
    # words = ["the", "day", "is", "sunny", "the",
    #          "the", "the", "sunny", "is", "is"]
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    print(Solution().topKFrequent(words, k))
            
