class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        smap,tmap = dict(), dict()
        for sc, tc in zip(s, t):
            if tc in tmap and sc != tmap[tc]:
                return False
            if sc in smap and tc != smap[sc]:
                return False
            tmap[tc] = sc
            smap[sc] = tc
        return True

if __name__ == '__main__':
    s = 'ab'
    t = 'aa'
    print(Solution().isIsomorphic(s, t))