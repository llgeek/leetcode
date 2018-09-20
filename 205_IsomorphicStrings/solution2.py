class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find, s) == map(t.find, t)

if __name__ == '__main__':
    s = 'ab'
    t = 'aa'
    print(Solution().isIsomorphic(s, t))
