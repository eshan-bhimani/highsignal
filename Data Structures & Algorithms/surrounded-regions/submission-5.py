class Solution:
    def solve(self, board: List[List[str]]) -> None:

        #so im thinking of looping through all the outer cells of the board, so the first row, last column, the last row, 
        if not board:
            return 0
        row, col = len(board), len(board[0])
        visited = set()
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == "O" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

            # Start from a border "O".
            # Explore connected "O"s using up/down/left/right.
            # Add them to visited because they are safe from capture.


#nested for loops to check for border Os, if border O and not in visited then run bfs
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r == 0 or r == row -1 or c == 0 or c == col - 1) and (r,c) not in visited:
                    bfs(r,c)

#nested for loops to check for non-border Os, if non-border O then mark "X"
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
