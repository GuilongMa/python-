class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        r1, c1 = 0, 0
        if not matrix:
            return []
        r2, c2 = len(matrix), len(matrix[0])
        new_matrix = []
        while r1 < r2 and c1 < c2:
            for c in range(c1, c2):
                new_matrix.append(matrix[r1][c])
            for r in range(r1+1, r2):
                new_matrix.append(matrix[r][c2-1])
            if r1 != r2 - 1:
                for c in range(c2-2, c1-1, -1):
                    new_matrix.append(matrix[r2-1][c])
            if c1 != c2 - 1:
                for r in range(r2-2, r1, -1):
                    new_matrix.append(matrix[r][c1])
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return new_matrix


class Solution_2:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        r1, c1 = 0, 0
        if not matrix:
            return []
        r2 = len(matrix) - 1
        c2 = len(matrix[0]) - 1
        new_matrix = []
        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2+1):
                new_matrix.append(matrix[r1][c])
            for r in range(r1+1, r2+1):
                new_matrix.append(matrix[r][c2])
            if r1 != r2:
                for c in range(c2-1, c1-1, -1):
                    new_matrix.append(matrix[r2][c])
            if c1 != c2:
                for r in range(r2-1, r1, -1):
                    new_matrix.append(matrix[r][c1])
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return new_matrix


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix))