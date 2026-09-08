class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        def dfs(i, memo= {}):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if i > n:
                return 0

            res =  dfs(i+1) + dfs(i+2)
            memo[i] = res   
            return res
            
        return dfs(0)  
         