"""
use fixed size heap with size k

time complexity O(N+Nlogk)
"""

class Word():
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        import heapq

        cnt = Counter(words)
        heap = []
        for word in cnt:
            heapq.heappush(heap, Word(word, cnt[word]))
            if len(heap) == k+1:
                heapq.heappop(heap)
        return [heapq.heappop(heap).word for _ in range(k)][::-1]


if __name__ == '__main__':
    #words = ["i", "love", "leetcode", "i", "love", "coding"]
    # words = ["the", "day", "is", "sunny", "the",
    #          "the", "the", "sunny", "is", "is"]
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    print(Solution().topKFrequent(words, k))
