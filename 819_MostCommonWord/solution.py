"""
corner cases like:

word[!?',;.]
word[!?',;.]word[!?',;.]word


so don't consider the punctuation will only exist after one word, and followed by a whitespace

use re for regular expression match,
replace or punctuations, and split words

"""


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # def filterpunc(word):
        #     word = word.lower()
        #     for p in "!?',;.":
        #         word = word.strip(p)
        #     if word in banned:
        #         return ''
        #     return word
        # from collections import Counter
        # banned = set(banned)
        # words = paragraph.strip().split()
        # # words = list(filter(lambda x: not any(map(lambda y: y in x, list("!?',;."))), words))
        # words = list(filter(lambda x: x not in "!?',;.", words))
        # words = map(filterpunc, words)
        # words = filter(None, words)
        # return Counter(words).most_common(1)[0][0]
        
        import re
        from collections import Counter
        paragraph = re.sub('[\W]', ' ', paragraph)
        words = paragraph.strip().split()
        words = map(str.lower, words)
        cnt = Counter(words)
        for word,_ in cnt.most_common():
            if word not in banned:
                return word


if __name__ == "__main__":
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # paragraph = "Bob. hIt, baLl"
    # banned = ["bob", "hit"]
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ['a']
    sol = Solution()
    print(sol.mostCommonWord(paragraph, banned))
        
