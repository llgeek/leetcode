import string
class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    order = dict(zip(order, string.ascii_lowercase))
    newwords = [str(map(order, word)) for word in words]
    for i in range(1, len(newwords)):
      if newwords[i] < newwords[i-1]:
        return False
    return True