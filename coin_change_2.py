class Solution:
    def change(self, amount, coins):
        memo = [0] * (amount + 1)
        memo[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                memo[x] += memo[x - coin]

        return memo[amount]
