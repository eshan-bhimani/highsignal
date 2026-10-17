class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        visit = set()
        islands = 0
        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                rows, cols = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    row, col = rows + dr, cols + dc
                    if 0 <= row < n and 0 <= col < m and grid[row][col] == "1" and (row, col) not in visit:
                        q.append((row, col))
                        visit.add((row, col))



        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands

        
        