from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        cnt1 = Counter(A.split(' '))
        cnt2 = Counter(B.split(' '))
        return list(filter(lambda x: x not in cnt2 and cnt1[x] == 1, cnt1)) + list(filter(lambda x: x not in cnt1 and cnt2[x] == 1, cnt2))
        

if __name__ == '__main__':
    A="this apple is sweet"
    B="this apple is sour"
    # A = "s z z z s"
    # B = "s z ejt"
    print(Solution().uncommonFromSentences(A, B))
