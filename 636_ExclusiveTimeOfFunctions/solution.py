from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if not logs: return []
        res = [0] * n
        stack = []
        prevtime = 0
        for log in logs:
          log = log.strip()
          if not log: continue
          log = log.split(":")
          idx, isstart, timestamp = int(log[0]), log[1] == "start", int(log[2])
          if isstart:
            if stack:
              res[stack[-1]] += (timestamp - prevtime)
            stack.append(idx)
            prevtime = timestamp
          else:
            res[idx] += timestamp - prevtime + 1
            prevtime = timestamp + 1
            stack.pop()
        return res
