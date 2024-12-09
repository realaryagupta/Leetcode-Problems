class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        # Initial boundaries
        top_left = 0
        top_right = len(matrix[0]) - 1
        bottom_left = 0
        bottom_right = len(matrix) - 1
        
        # Traverse the matrix in spiral order
        while top_left <= bottom_right and bottom_left <= top_right:
            # Traverse from left to right along the top row
            for i in range(top_left, top_right + 1):
                ans.append(matrix[bottom_left][i])
            
            # Traverse from top to bottom along the right column
            for i in range(bottom_left + 1, bottom_right + 1):
                ans.append(matrix[i][top_right])
            
            # Traverse from right to left along the bottom row (if still within bounds)
            if bottom_left < bottom_right:
                for i in range(top_right - 1, top_left - 1, -1):
                    ans.append(matrix[bottom_right][i])
            
            # Traverse from bottom to top along the left column (if still within bounds)
            if top_left < top_right:
                for i in range(bottom_right - 1, bottom_left, -1):
                    ans.append(matrix[i][top_left])
            
            # Move the boundaries inward
            top_left += 1
            top_right -= 1
            bottom_left += 1
            bottom_right -= 1
        
        return ans
