count = 0


# 列表result下标表示行，数值表示列
def cal8queues(result, row):
    if row == 8:
        global count
        count += 1
        print_queues(result)
        return
    for col in range(8):
        if is_ok(result, row, col):
            result[row] = col
            cal8queues(result, row+1)


def print_queues(result):
    # new_result = []
    # for i, j in enumerate(result):
    #     new_result.append((i, j))
    # print(new_result)
    for row in range(8):
        for col in range(8):
            if result[row] == col:
                print("Q ", end='')
            else:
                print("* ", end='')
        print('\n', end='')
    print("\n")


def is_ok(result, row, col):
    left_up = col - 1
    right_up = col + 1
    for i in range(row-1, -1, -1):
        if result[i] == col:
            return False
        if 0 <= left_up:
            if left_up == result[i]:
                return False
        if 8 >= right_up:
            if right_up == result[i]:
                return False
        left_up += 1
        right_up += 1
    return True


if __name__ == "__main__":
    r= ["*"] * 8
    cal8queues(r, 0)
    print(count)