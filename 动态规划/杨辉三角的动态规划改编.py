import copy
min_length = 100
count = 0


# 回溯实现 row,col初始值为0， length:当前路径长度,初始值为5， nums_list:数组
def back_track(row, col, length, nums_list):
    # print(nums_list[row][col])
    global min_length
    if row == 4:
        global count
        count += 1
        if length < min_length:
            min_length = length
        return

    back_track(row+1, col, length+nums_list[row+1][col], nums_list)
    back_track(row+1, col+1, length+nums_list[row+1][col+1], nums_list)


def dynamic1(nums_list):
    # 建立跟matrix一样的状态表
    states = copy.deepcopy(nums_list)
    for i in range(len(nums_list)):
        for j in range(len(nums_list[i])):
            states[i][j] = None
    states[0][0] = nums_list[0][0]
    for i in range(1, len(nums_list)):
        for j in range(len(nums_list[i])):
            if j == 0:
                states[i][j] = states[i-1][j] + nums_list[i][j]
            elif j == len(nums_list[i]) - 1:
                states[i][j] = states[i-1][j-1] + nums_list[i][j]
            else:
                top1 = states[i-1][j-1]
                top2 = states[i-1][j]
                states[i][j] = min(top1, top2) + nums_list[i][j]
    print(states)
    return min(states[-1])


# 动态规划实现
def dynamic2(matrix):
    # 建立跟matrix一样的状态表
    states = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            states[i][j] = None

    # 初始化状态表第一列
    for i in range(len(matrix)):
        sums = 0
        for j in range(i+1):
            sums += matrix[j][0]
        states[i][0] = sums

    # 初始化状态表第一行
    for i in range(len(matrix[0])):
        sums = 0
        for j in range(i+1):
            sums += matrix[0][j]
        states[0][i] = sums

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-i):
            states[i][j] = matrix[i][j] + min(states[i-1][j], states[i][j-1])

    return min([i[-1] for i in states])


if __name__ == "__main__":
    # 回溯
    nums_list = [[5], [7, 8], [2, 3, 4], [4, 9, 6, 1], [2, 7, 9, 4, 5]]
    back_track(0, 0, 5, nums_list)
    print(min_length)
    # print(count)
    # 动态规划1
    print(dynamic1(nums_list))

    # 动态规划2
    matrix = [[5, 8, 4, 1, 5], [7, 3, 6, 4], [2, 9, 9], [4, 7], [2]]
    print(dynamic2(matrix))

