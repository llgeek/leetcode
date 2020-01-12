# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def match(word1, word2):
            return sum(1 if c1 == c2 else 0 for c1, c2 in zip(word1, word2))
        
        for _ in range(10):
            cnt = [0] * len(wordlist)
            for i in range(len(wordlist)):
                for j in range(len(wordlist)):
                    if i == j: continue
                    if match(wordlist[i], wordlist[j]) == 0:
                        cnt[i] += 1
            candidate, unmatchcnt = wordlist[0], len(wordlist)
            for i in range(len(wordlist)):
                if unmatchcnt > cnt[i]:
                    candidate = wordlist[i]
                    unmatchcnt = cnt[i]
            x = master.guess(candidate)
            if x == len(wordlist[0]): break    # find the answer
            nextwordlist = []
            for word in wordlist:
                if match(word, candidate) == x:
                    nextwordlist.append(word)
            wordlist = nextwordlist[:]


