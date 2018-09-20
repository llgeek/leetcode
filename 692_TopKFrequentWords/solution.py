from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        #return sorted([k for k, v in Counter(words).most_common(k)])
        return [k for k, v in sorted(Counter(words).most_common(), key = lambda x: (-x[1], x[0]))][:k]


if __name__ == '__main__':
    #words = ["i", "love", "leetcode", "i", "love", "coding"]
    # words = ["the", "day", "is", "sunny", "the",
    #          "the", "the", "sunny", "is", "is"]
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    print(Solution().topKFrequent(words, k))
