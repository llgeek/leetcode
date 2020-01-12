from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        cnt = {}
        w = ''
        for c in paragraph:
            if c.isalpha():
                w = w + c
            else:
                w = w.lower()
                if w and w not in banned:
                    cnt[w] = cnt.get(w, 0) + 1
                w = ''
        w = w.lower()
        if w and w not in banned:
            cnt[w] = cnt.get(w, 0) + 1
        ans = '', 0
        for key, value in cnt.items():
            if value > ans[1]:
                ans = key, value
        return ans[0]

if __name__ == "__main__":
    sol = Solution()
    # paragraph = "a, a, a, a, b,b,b,c, c"
    # banned = ["a"]
    paragraph = "Bob. hIt, baLl"
    banned = ["bob", "hit"]
    print(sol.mostCommonWord(paragraph, banned))