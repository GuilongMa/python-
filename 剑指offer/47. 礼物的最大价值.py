class Solution:
    def maxValue(self, grid: [[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        def fc(r1, c1):
            if r1 == 0 and c1 == 0:
                return grid[r1][c1]
            elif c1 == 0:
                return fc(r1-1, c1) + grid[r1][c1]
            elif r1 == 0:
                return fc(r1, c1-1) + grid[r1][c1]
            else:
                return max(fc(r1-1, c1), fc(r1, c1-1)) + grid[r1][c1]
        return fc(r-1, c-1)


class Solution2:
    def maxValue(self, grid: [[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        states = [[0 for i in range(c)] for j in range(r)]
        sums = 0
        # 初始化第一行
        for col in range(c):
            sums += grid[0][col]
            states[0][col] = sums
        sums = 0
        # 初始化第一列
        for row in range(r):
            sums += grid[row][0]
            states[row][0] = sums

        for r1 in range(1, r):
            for c1 in range(1, c):
                states[r1][c1] = max(states[r1 - 1][c1], states[r1][c1 - 1]) + grid[r1][c1]

        return states[r - 1][c - 1]


if __name__ == "__main__":
    sol = Solution2()
    matrix = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(sol.maxValue(matrix))