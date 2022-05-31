max_val = 0
max_result = []
count = 0


def bag_of_0and1(result, n, goods, w, good):
    if good == n:
        print_bag(result, goods)
        return
    for i in range(2):
        if is_ok(i, good, result, goods, w):
            result[good] = i
            if good == n - 1:
                global max_val, max_result, count
                count += 1
                max_result = result
                max_val = max(max_val, sum([result[i]*goods[i][1] for i in range(len(result))]))
            bag_of_0and1(result, n, goods, w, good+1)


def print_bag(result, goods):
    w, v = zip(*goods)
    sum_w = sum([result[i] * w[i] for i in range(len(result))])
    sum_val = sum([result[i] * v[i] for i in range(len(result))])
    print(w)
    print(result)
    print(sum_w)
    print(v)
    print(result)
    print(sum_val)
    print("\n")


def is_ok(flag, good, result, goods, w):
    sum_w = 0
    for i in range(good):
        sum_w += result[i] * goods[i][0]
    sum_w += flag * goods[good][0]
    if sum_w <= w:
        return True
    else:
        return False


# 0/1背包简化:在不超过限制下，求包中物品的最大重量
maxW = 0


# i表示第几个物品，cw当前装进去的物品重量和，items表示每个物品的重量
# n表示物品个数， w表示重量限制
def f(i, cw, items, n, w):
    # 剪枝，当重量>=w，则不再探索剩下的物品
    if cw == w or i == n:
        global maxW
        if cw > maxW:
            maxW = cw
        return
    # 枚举
    for j in range(2):
        new_cw = cw + j * items[i]
        if new_cw <= w:
            f(i+1, new_cw, items, n, w)

    # 等价于上面实现
    # f(i+1, cw, items, n, w)
    # if cw + items[i] <= w:
    #     f(i+1, cw+items[i], items, n, w)


def f2(i, cw, items, n, w):
    # 剪枝，当重量>=w，则不再探索剩下的物品
    if cw == w or i == n:
        global maxW
        if cw > maxW:
            maxW = cw
        return
    # # 枚举
    # for j in range(2):
    #     new_cw = cw + j * items[i]
    #     if new_cw <= w:
    #         f(i + 1, new_cw, items, n, w)

    # 等价于上面实现
    f2(i+1, cw, items, n, w)
    if cw + items[i] <= w:
        f2(i+1, cw+items[i], items, n, w)


def f3(i, cw, items, n, w):
    # 剪枝，当重量>=w，则不再探索剩下的物品
    if cw == w or i == n:
        global maxW
        if cw > maxW:
            maxW = cw
        return

    if cw + items[i] <= w:
        f3(i+1, cw+items[i], items, n, w)
    f3(i+1, cw, items, n, w)


if __name__ == "__main__":
    # num = 6
    # goods = [(1, 3), (2, 4), (4, 5), (6, 9), (7, 7), (10, 20)]
    # w = 20
    # r = [None] * 6
    # bag_of_0and1(r, num, goods, w, 0)
    # print(count)
    # print(max_result)
    # print(max_val)

    i = 0
    cw = 0
    items = [1, 5, 6, 7, 13, 18]
    n = 6
    w = 100
    f(i, cw, items, n, w)
    print(maxW)
    f2(i, cw, items, n, w)
    print(maxW)
    f3(i, cw, items, n, w)
    print(maxW)
