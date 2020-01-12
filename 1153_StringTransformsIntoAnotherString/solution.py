class Solution():
    def if_transformable(self, str1, str2):
        """
        return type: boolean
        """
        if len(str1) != len(str2):
            return False
        
        have = set()
        change = {}
        for i in range(len(str1)):
            have.add(str2[i])
            if str1[i] not in change:
                change[str1[i]] = str2[i]
            if change[str1[i]] != str2[i]:
                return False
        return len(change) >= len(have) and (len(have) < 26 or str1 == str2)


if __name__ == "__main__":
    sol = Solution()
    str1 = "aabcc"
    str2 = "ccdee"
    str1 = "leetcode"
    str2 = "codeleet"
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "bcdefghijklmnopqrstuvwxyza"
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "bbcdefghijklmnopqrstuvwxyz"
    print(sol.if_transformable(str1, str2))