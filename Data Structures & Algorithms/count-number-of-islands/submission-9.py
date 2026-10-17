class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: #empty grid, base case return 0
            return 0
        visited = set() #visited set that all bfs calls share, tells all discovered cells
        row, col = len(grid), len(grid[0]) #initializes rows and columns
        islands = 0

        def bfs(r, c): #explore the entire island starting here
            q = collections.deque() #queue of cells waiting to be explored
            visited.add((r,c)) #mark starting cells as discovered
            q.append((r,c)) #add starting cell to queue
            while q: #continue until no cells are waiting in queue
                r, c = q.popleft() #remove oldest cell to explore its neighbors
                directions = [[1,0],[-1,0], [0,1], [0,-1]] #down, up, right, left
                for dr, dc in directions: #check each of 4 directions
                    nr, nc = r + dr, c + dc #neighbor coordinates, keep r and c unchanged
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1" and (nr,nc) not in visited: # neighbors row in bounds, neighbors col in bounds, if neighbor in land, if neighbor hasnt been discovered yet
                        visited.add((nr,nc)) #mark new to prevent duplicate enqueues
                        q.append((nr,nc)) #explore this neighbor later
                        





        for r in range(row): #scan every row
            for c in range(col): #scan every col
                if grid[r][c] == "1" and (r,c) not in visited: #find unvisited land
                    bfs(r, c) #mark every land cell in this island
                    islands += 1 #one BFS call discovers 1 new island
        return islands #total number of islands
        