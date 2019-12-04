class Solution:
    def nextClosestTime(self, time):
      num = list(map(int, time[:2] + time[3:]))
      h = int(time[:2])
      m = int(time[3:])
      self.best = to_time(h, m)
      

      def to_time(h, m):
        return h * 60 + m
      def time_diff(t1, t2):
        if t1 == t2: return (1<<31) - 1
        return t1 - t2
      
      def dfs()