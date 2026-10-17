class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
            return -1
        visited = set()

        def bfs(r,c):
            minPath =  1
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                for _ in range(len(q)): #all cells at the same path length
                    r, c = q.popleft()
                    if (r,c) == (row - 1, col - 1):
                        return minPath
                    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 0 and (nr,nc) not in visited:
                            q.append((nr,nc))
                            visited.add((nr,nc))
                minPath += 1
        
            return -1

        
        return bfs(0,0)
        