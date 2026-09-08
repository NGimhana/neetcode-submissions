class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dfs(i, nums, memo=None):
            if memo is None:
                memo = {}
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            
            result = max(dfs(i+1,nums,memo), nums[i] + dfs(i+2,nums,memo))
            memo[i] = result
            return result
        
        
        return max(dfs(0, nums[:-1]), dfs(0, nums[1:]))
