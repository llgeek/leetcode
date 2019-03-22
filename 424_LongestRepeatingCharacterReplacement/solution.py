class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        import string
        res = 0
        # preidx = {c:0 for c in 'abcdefghijklmnopqrstuvwxyz'.upper()}
        preidx = {c: 0 for c in string.ascii_uppercase}
        accnum = {c: 0 for c in string.ascii_uppercase}
        prechar = s[0]
        for i, c in enumerate(s):
            accnum[c] += 1
            j = preidx[c]
            while (i-preidx[c]+1 > accnum[c]+k):
                if s[j] == c:
                    # preidx[c] = j
                    accnum[c] -= 1
                j += 1
                preidx[c] = j
            # res = max(res, i-preidx[c]+1)
            if i-preidx[prechar] + 1 <= accnum[prechar]+k and i-preidx[prechar] > i-preidx[c]:
                res = max(res, i-preidx[prechar]+1)
            elif i-preidx[c]+1 > res:
                prechar = c
                res = max(res, i-preidx[c]+1)
        return res




if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    # s = "ABAB"
    # k = 2
    # s = "BAAAB"
    # k = 2
    sol = Solution()
    print(sol.characterReplacement(s, k))


