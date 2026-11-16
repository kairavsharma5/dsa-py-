class Solution(object):
    def findPeakGrid(self, mat):
        n, m = len(mat), len(mat[0])      # n = rows, m = columns
        low, high = 0, m - 1

        def max_row(col):
            # row index of the largest element in this column
            row = 0
            for i in range(n):
                if mat[i][col] > mat[row][col]:
                    row = i
            return row

        while low <= high:
            mid = (low + high) // 2
            row = max_row(mid)

            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1]