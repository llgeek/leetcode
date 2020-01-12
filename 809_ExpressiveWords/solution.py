class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def get_groups(word):
            i, j = 0, 0
            groups = []
            chrset = []
            while j < len(word):
                if word[j] != word[i]:
                    groups.append(word[i:j])
                    chrset.append(word[i])
                    i = j
                j += 1
            if i != j:
                groups.append(word[i:j])
                chrset.append(word[i])
            return groups, chrset

        def stretchy(word):
            word_groups, word_chrset = get_groups(word)
            if word_chrset != S_chrset:
                return False
            
            for i in range(len(word_groups)):
                if word_groups[i] == S_groups[i]:
                    continue
                if len(word_groups[i]) > len(S_groups[i]):
                    return False
                if len(S_groups[i]) < 3:
                    return False
            return True

        S_groups, S_chrset = get_groups(S)
        return sum(stretchy(word) for word in words)