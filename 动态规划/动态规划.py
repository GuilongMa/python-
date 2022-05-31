def min_dist_dp(matrix, n):
    states = [[None]*n] * n
    sums = 0
    # 初始化第一行
    for col in range(n):
        sums += matrix[0][col]
        states[0][col] = sums

    sums = 0
    # 初始化第一列
    for row in range(n):
        sums += matrix[row][0]
        states[row][0] = sums

    for i in range(1, n):
        for j in range(1, n):
            states[i][j] = matrix[i][j] + min(states[i-1][j], states[i][j-1])

    return states[n-1][n-1]


if __name__ == "__main__":
    matrix = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    print(min_dist_dp(matrix, 4))
