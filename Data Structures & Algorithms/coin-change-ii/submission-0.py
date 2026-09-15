    
class Solution:


    def change(self, amount: int, coins: List[int]) -> int:
        # dp[current_amount] stores the number of combinations for current_amount.
        dp = [0] * (amount + 1)

        # There is one way to create amount zero: choose no coins.
        dp[0] = 1

        # Process each denomination once to prevent counting different orders.
        for coin in coins:
            # Traverse forward because each coin can be used unlimited times.
            for current_amount in range(coin, amount + 1):
                # Add combinations that form the remaining amount after using coin.
                dp[current_amount] += dp[current_amount - coin]

        # Return zero automatically if the target cannot be formed.
        return dp[amount]