class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [""]
        mapping = {1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
                  6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0: ''}
        idx = 0
        while idx < len(digits):
          nextres = []
          for pre in res:
            for c in mapping[int(digits[idx])]:
              nextres.append(pre+c)
          res = nextres[:]
          idx += 1
        return [] if not any(res) else res
