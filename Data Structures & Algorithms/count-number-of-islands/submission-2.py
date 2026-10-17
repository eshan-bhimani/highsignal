class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visit = set()
        n, m = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands  
        