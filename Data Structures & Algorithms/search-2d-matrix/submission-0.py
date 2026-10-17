class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            l, r = 0, col - 1
            mid = (l + r) // 2
            while l <= r:
                if matrix[i][mid] < target:
                    l = mid + 1
                    mid = (l + r) // 2
                if matrix[i][mid] > target:
                    r = mid - 1
                    mid = (l + r) // 2
                if matrix[i][mid] == target:
                    return True
        
        return False





        