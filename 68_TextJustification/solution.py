class Solution:
    def fullJustify(self, words, maxWidth: int):
        res = []
        i = 0
        while i < len(words):
            l, k = 0, 0
            while i + k < len(words) and l + len(words[i+k]) <= maxWidth - k:
                l += len(words[i+k])
                k += 1
            
            tmp = words[i]
            for j in range(k-1):
                if i + k >= len(words):
                    tmp += ' '
                else:
                    tmp += ' ' * ((maxWidth - l) // (k - 1) + (j < (maxWidth - l) % (k-1)))
                tmp += words[i+j+1]
            tmp += ' ' * (maxWidth - len(tmp))
            res.append(tmp)
            i += k
        return res

if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
        "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    sol = Solution()
    print(sol.fullJustify(words, maxWidth))
