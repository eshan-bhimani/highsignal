class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            count = 1
            visited.add((r,c))
            q.append((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr, nc))
                        count += 1
            return count

                    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea