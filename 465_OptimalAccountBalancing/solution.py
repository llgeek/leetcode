from collections import defaultdict
class Solution:
    def minimal_trans(self, transactions):
        def helper(debts, pos, act):
            while pos < len(debts) and debts[pos] == 0:
                pos += 1
            if pos == len(debts):
                self.res = min(self.res, act)
                return
            for i in range(pos + 1, len(debts)):
                if debts[pos] ^ debts[i] < 0:
                    debts[i] += debts[pos]
                    helper(debts, pos+1, act+1)
                    debts[i] -= debts[pos]

        balance = defaultdict(lambda: 0)
        self.res = (1 << 31) - 1
        for t in transactions:
            balance[t[0]] += t[2]
            balance[t[1]] -= t[2]
        debts = []
        for p in balance:
            if balance[p] != 0:
                debts.append(balance[p])
        helper(debts, 0, 0)
        return self.res

if __name__ == "__main__":
    sol = Solution()
    # transactions = [[0,1,10], [2,0,5]]
    transactions = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
    print(sol.minimal_trans(transactions))

