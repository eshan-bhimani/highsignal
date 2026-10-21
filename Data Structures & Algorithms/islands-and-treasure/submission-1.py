class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return
        q = collections.deque()
        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))
        def bfs(r,c):
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))


        bfs(r,c)
                