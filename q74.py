from turtle import left, right
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        N = rows * cols

        left = 0
        right = N - 1

        while left <= right:
            middle = (left + right) // 2
            i = middle // cols
            j = middle % cols

            if matrix[i][j] < target:
                left = middle + 1
            elif matrix[i][j] > target:
                right = middle - 1
            else:
                return True
        
        return False


    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        if rows == 2:
            if matrix[1][0] > target:
                target_row = 0
            else:
                target_row = 1
        
        elif rows == 1:
            target_row = 0
        else:
            while bottom-top > 1:
                mid = (top + bottom) // 2
                if matrix[mid][0] > target:
                    bottom = mid
                elif matrix[mid][0] < target:
                    top = mid
                else:
                    return True
            
            if matrix[bottom][0] <= target:
                target_row = bottom
            else:
                target_row = top

        left = 0
        right = cols - 1

        while right-left > 1:
            mid = (left + right) // 2
            if matrix[target_row][mid] > target:
                right = mid
            elif matrix[target_row][mid] < target:
                left = mid
            else:
                return True
        
        return matrix[target_row][left] == target or matrix[target_row][right] == target
            

if __name__ == '__main__':
    matrix = [[1,1]]
    target = 2
    s = Solution()
    print(s.searchMatrix(matrix=matrix, target=target))