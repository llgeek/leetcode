class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    orderdict = {key: idx for idx, key in enumerate(order)}
    def compare(w1, w2):
      i, j = 0, 0
      while i < len(w1) and j < len(w2):
        if orderdict[w1[i]] > orderdict[w2[j]]: return False
        elif orderdict[w1[i]] < orderdict[w2[j]]: return True
        else:
          i += 1
          j += 1
      return not (i < len(w1) and j == len(w2))
    
    for idx in range(1, len(words)):
      if not compare(words[idx-1], words[idx]): return False
    return True
