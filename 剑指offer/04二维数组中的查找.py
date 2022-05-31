class Solution:
    def findNumberIn2DArray(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        r = 0
        c = m - 1
        while r < n and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False


if __name__ == "__main__":
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

    sol = Solution()
    print(sol.findNumberIn2DArray(matrix, 5))