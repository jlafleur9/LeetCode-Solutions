class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) 
        COLS = len(matrix[0]) # this line gets the length of the first list
        
        
        
        bottom = ROWS - 1
        top = 0
        
        while top <= bottom:
            row = (top + bottom) // 2 #Pick the middle row
            if target > matrix[row][-1]:
                #matrix of our middle row and -1 is the last index of that row, so the end of the list
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        if not(top <= bottom):
            return False
                
        left = 0
        right = COLS - 1 
        row = (top + bottom) // 2
        
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            if target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False 