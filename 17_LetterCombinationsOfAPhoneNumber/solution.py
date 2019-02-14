"""
time complexity: O(n*3)
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """ 
        digit2alp = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        for c in digits:
            tmpres = []
            for alp in digit2alp[c]:
                if not res:
                    tmpres.append(alp)
                else:
                    for pre in res:
                        tmpres.append(pre+alp)
            res = tmpres.copy()
        return res

            
if __name__ == "__main__":
    digits = '23'
    sol = Solution()
    print(sol.letterCombinations(digits))