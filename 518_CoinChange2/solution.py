class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        nums = [0 for _ in range(amount+1)]
        nums[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                nums[j] += nums[j - coins[i]]
        return nums[amount]

if __name__ == '__main__':
    amount = 10
    coins = [3]
    print(Solution().change(amount, coins))