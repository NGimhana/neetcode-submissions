from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # empty grid
        if not grid:
            return 0
        
        ## dimentions
        ROWS, COLUMNS = len(grid), len(grid[0])
        visited = set()

        islands = 0
        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                row,col = queue.popleft()
                ## check adjus
                directions = [[0,1], [0,-1], [-1,0], [1,0]]
                for dr, dc in directions:
                    r, c = row + dr , col + dc
                    if (r >=0 and r<ROWS and c >=0 and c<COLUMNS and grid[r][c] =="1" and (r,c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))



        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands



        