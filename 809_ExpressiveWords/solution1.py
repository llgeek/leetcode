from typing import List
import itertools
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def get_groups(word):
            return [(k, len(list(K))) for k, K in itertools.groupby(word)]

        def stretchy(word):
            word_groups = get_groups(word)
            if len(word_groups) != len(S_groups):
                return False
            for i in range(len(word_groups)):
                if word_groups[i][0] != S_groups[i][0] or word_groups[i][1] > S_groups[i][1] or \
                        (S_groups[i][1] < 3 and word_groups[i][1] != S_groups[i][1]):
                    return False
            return True
        S_groups = get_groups(S)
        return sum(stretchy(word) for word in words)

if __name__ == "__main__":
    sol = Solution()
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(sol.expressiveWords(S, words))