class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return 0
        
        if amount in coins:
            return 1

        total = 0
        count = 0

        def dfs(amount, memo=None):
            
            if memo is None:
                memo = {}

            if amount in memo:
                return memo[amount] 

            if amount == 0:
                return 0

            res = float("inf")

            for coin in coins:
                if amount - coin >=0:
                    remaininRes= dfs(amount-coin, memo)
                    memo[amount] = remaininRes
                    res = min(res, 1+ remaininRes)
            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= float("inf") else minCoins