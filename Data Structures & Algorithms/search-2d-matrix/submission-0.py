class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n -1

        while l <= r:
            m = (l + r) // 2
            row = m // n
            col = m % n
            mid_val = matrix[row][col]
            if mid_val < target:
                l = m + 1
            elif mid_val > target:
                r = m - 1
            elif mid_val == target:
                return True
        return False