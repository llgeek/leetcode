# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def dist(word1, word2):
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        def most_overlap_word(wordlist):
            overlap = [[0 for _ in range(26)] for _ in range(6)]
            for word in wordlist:
                for i, c in enumerate(word):
                    overlap[i][ord(c) - ord('a')] += 1
                
            candidate, score = '', 0
            for word in wordlist:
                wordscore = 0
                for i, c in enumerate(word):
                    wordscore += overlap[i][ord(c) - ord('a')]
                if wordscore > score:
                    candidate, score = word, wordscore
            
            return candidate

        while wordlist:
            candidate = most_overlap_word(wordlist)
            x = master.guess(candidate)
            if x == len(candidate):
                break
            
            wordlist = [word for word in wordlist if dist(word, candidate) == x]