class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            j = 0
            k = len(matrix[0]) - 1

            while j <= k:
                mid = (j + k) // 2

                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    j = mid + 1
                else:
                    k = mid - 1
            
        return False