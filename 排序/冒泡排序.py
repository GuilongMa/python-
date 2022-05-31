# 原地排序
def mao_pao_sort(temp):
    if len(temp) <= 1:
        return temp
    for time in range(len(temp) - 1):
        swap_flag = False
        for index in range(len(temp) - time - 1):
            if temp[index] > temp[index + 1]:
                temp[index], temp[index + 1] = temp[index + 1], temp[index]
                swap_flag = True
        if not swap_flag:
            break
    return temp


if __name__ == "__main__":
    L1 = [1, 2, 2, 4, 3]
    L2 = [4, 3, 2, 6, 5, 8, 7, 9, 1]
    print(maopao_sort(L1))
    print(maopao_sort(L2))
