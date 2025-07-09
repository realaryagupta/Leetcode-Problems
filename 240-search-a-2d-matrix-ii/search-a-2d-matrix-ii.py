class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        # start from top right corner
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                # reduce col
                col = col - 1

            else:
                # increase row
                row = row + 1

        return False