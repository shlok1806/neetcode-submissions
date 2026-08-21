class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        hi = ROWS * COLS - 1
        low = 0 

        while hi >= low:
            mid = (hi + low) // 2
            r = mid // COLS
            c = mid % COLS
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                hi = mid - 1
            else:
                low = mid + 1
        
        return False