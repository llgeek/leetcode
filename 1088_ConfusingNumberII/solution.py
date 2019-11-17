
class Solution():
  def findAllConfNums(self, n):
    validnum = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
    invalidnum = {2, 3, 4, 5, 7}

    def check(num):
      prenum = num
      newnum = 0
      while num:
        num, mod = divmod(num, 10)
        newnum = newnum * 10 + validnum[mod]
      return newnum != prenum

    res = 0
    nodes = [1, 6, 8, 9]
    while nodes:
      last = nodes.pop()
      if last <= n:
        if check(last):
          res += 1
        for key in validnum.keys():
          nextval = last * 10 + key
          if nextval <= n:
            nodes.append(nextval)
    return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.findAllConfNums(1000000000))
