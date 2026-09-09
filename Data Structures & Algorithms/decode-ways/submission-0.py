class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        def dfs(i, memo=None):
            
            if memo is None:
                memo = {}

            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            

            res = dfs(i+1, memo)
            memo[i] = res

            if i < len(s)-1:
                if (s[i] == "1") or (s[i] == "2" and s[i+1]<"7"):
                    res += dfs(i+2, memo)
                    memo[i] = res 
            return res
        return dfs(0)