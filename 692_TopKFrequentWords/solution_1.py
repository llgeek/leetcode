"""
O(N + klogN) time complexity, heapify takes O(N), heappop takes O(logN)

"""

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import heapq
        from collections import Counter
        cnt = Counter(words)
        # heap = []
        # for word in cnt:
        #     heapq.heappush(heap, (-cnt[word], word))
        # return [heapq.heappop(heap)[1] for _ in range(k)]
        heap = [(-cnt[word], word) for word in cnt]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == '__main__':
    #words = ["i", "love", "leetcode", "i", "love", "coding"]
    # words = ["the", "day", "is", "sunny", "the",
    #          "the", "the", "sunny", "is", "is"]
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    print(Solution().topKFrequent(words, k))
