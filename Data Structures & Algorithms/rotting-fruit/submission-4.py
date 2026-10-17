class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        row, col = len(grid), len(grid[0])

        def bfs():
            q = collections.deque()
            fresh = 0
            minute = 0
            for r in range(row):
                for c in range(col):
                    if grid[r][c] == 2:
                        q.append((r,c))
                    elif grid[r][c] == 1:
                        fresh +=1
            while q and fresh > 0:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            fresh -= 1
                minute += 1
            return minute if fresh == 0 else -1


        return bfs()

        
        