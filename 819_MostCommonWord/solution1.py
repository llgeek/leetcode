"""
don't try to come up with fancy and short solution
just literarily process the character one by one

scan the paragraph for once
"""


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import defaultdict
        banned = set(banned)
        words = defaultdict(lambda : 0)
        word = ''
        for c in paragraph:
            if c.isalpha():
                word += c 
            else:
                if word:
                    words[word.lower()] += 1
                    word = ''
        if word:
            words[word.lower()] += 1
        maxnum = 0
        retword = ''
        for word, num in words.items():
            if word not in banned and num > maxnum:
                maxnum = num
                retword = word
        return retword

if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    # paragraph = "Bob. hIt, baLl"
    # banned = ["bob", "hit"]
    # paragraph = "a, a, a, a, b,b,b,c, c"
    # banned = ['a']
    sol = Solution()
    print(sol.mostCommonWord(paragraph, banned))
