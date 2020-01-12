# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def dist(word1, word2):
            # return sum(1 if c1 == c2 else 0 for c1, c2 in zip(word1, word2))
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))
        
        def get_max_dist_candidate(candidate, wordlist):
            hist = [0] * len(candidate)
            for word in wordlist:
                hist[dist(candidate, word)] += 1
            return max(hist)

        def get_min_max_dist_candidate(wordlist):
            candidate, dist = wordlist[0], len(wordlist)
            for i in range(1, len(wordlist)):
                cur_dist = get_max_dist_candidate(candidate, wordlist[i])
                if cur_dist < dist:
                    candidate, dist = wordlist[i], cur_dist
            return candidate

        while wordlist:
            candidate = get_min_max_dist_candidate(wordlist)
            x = master.guess(candidate)
            if x == len(candidate):
                break
            next_wordlist = []
            for i in range(len(wordlist)):
                if dist(candidate, wordlist[i]) == x:
                    next_wordlist.append(wordlist[i])
            wordlist = next_wordlist[:]
