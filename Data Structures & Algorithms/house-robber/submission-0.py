class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i, memo = {}):
            if i in memo:
                 return memo[i]
            if i >= len(nums):
                return 0
            
            ## two choises
            ## pick current i, money = current house money + i+2 house money
            ## not pick current house i rob it
            ## select the maximum robbed money
            result = max(dfs(i+1), nums[i] + dfs(i+2))
            memo[i] = result
            return result

        return dfs(0)