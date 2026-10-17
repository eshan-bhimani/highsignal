class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        row, col = len(grid), len(grid[0])
        maxIsland = 0
        def bfs(r,c):
            islandArea = 1
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        islandArea += 1               
            return islandArea
        #maxIsland = max(maxIsland, islandArea)



        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxIsland = max(maxIsland, bfs(r,c))

        return maxIsland
        



        