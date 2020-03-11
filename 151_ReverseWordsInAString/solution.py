class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        word = ''
        for c in s:
            if c == ' ':
                if word:
                    res.append(word)
                    word = ''
                continue
            word = word + c
        if word:
            res.append(word)
        return " ".join(res[::-1])
                
