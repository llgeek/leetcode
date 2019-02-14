"""
bottom up way

time O(len(coins) * amount)
"""


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        changes = [-1] * (amount+1)
        changes[0] = 0
        for num in range(amount+1):
            res = amount+1
            for coin in coins:
                if num - coin >= 0 and changes[num-coin] != -1:
                    res = min(res, changes[num-coin] + 1)
            if res != amount+1:
                changes[num] = res
        return changes[amount]

if __name__ == "__main__":
    # coins = [1, 2, 5]
    # amount = 11
    # coins = [2]
    # amount = 3
    coins = [2147483647]
    amount = 2
    sol = Solution()
    print(sol.coinChange(coins, amount))
        
        

