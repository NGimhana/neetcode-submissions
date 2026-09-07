class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLUMNS = len(board), len(board[0])
        visited = set()

        # current char in the word
        def dfs(r,c, i):
            if i == len(word):
                return True
            if (r <0 or r == ROWS or c<0 or c == COLUMNS or board[r][c] != word[i] or (r,c) in visited):
                return False

            ## found a path
            visited.add((r,c))
            

            ## we already know the ith position
            res =  (dfs(r,c+1, i+1) or
            dfs(r+1,c,i+1) or
            dfs(r-1,c,i +1)or
            dfs(r,c-1,i + 1))
            

            visited.remove((r,c))
            return res 
        
        for i in range(ROWS):
            for j in range(COLUMNS):
                if dfs(i,j,0):
                    return True
        return False