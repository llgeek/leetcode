from typing import List
class Solution:
    MAPPING = {'1': '', '2': 'abc', '3':'def', '4' : 'ghi', '5': 'jkl', '6' : 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0':''}
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        for i in range(len(digits)):
            tmpres = []
            for c in self.MAPPING[digits[i]]:
                if res:
                    for pre in res:
                        tmpres.append(pre+c)
                else:
                    tmpres.append(c)
            res = tmpres[:]
        return res 
        