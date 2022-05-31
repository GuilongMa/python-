coins_list = [1, 3, 5]
w = 9
# 初始值取最大，100是方便测试
min_count = 100
cache_list = [False] * 10


# 回溯实现
# n表示硬币种类, cur_w表示当前硬币总和价值, count表示当前硬币个数
def count_of_coin(cur_w, count):
    global w, coins_list, min_count

    # 剪裁
    if cache_list[cur_w]:
        if cache_list[cur_w] < count:
            return
        else:
            cache_list[cur_w] = count
    cache_list[cur_w] = count

    if cur_w == w:
        if count < min_count:
            min_count = count
        return

    for i in coins_list:
        if cur_w + i <= w:
            count_of_coin(cur_w+i, count+1)


# 动态规划实现:状态表转移
def count_of_coin2():
    global w, coins_list, min_count
    states = [None] * (w+1)
    # 初始化states第一行
    for i in coins_list:
        states[i] = True

    max_count = w // min(coins_list)
    for i in range(1, max_count):
        for j in range(w-1, -1, -1):
            if states[j]:
                for k in coins_list:
                    if j + k == w:
                        return i + 1
                    elif j + k < w:
                        states[j+k] = True
                    else:
                        continue
    return None


# 状态转移方程法
def count_of_coin3(money):
    states = [0, 1, 2, 1, 2, 1]
    if money < 6:
        return states[money]

    for i in range(6, money+1):
        states[i] = 1 + min(states[i-1], states[i-3], states[i-5])

    return states[money]


if __name__ == "__main__":
    count_of_coin(0, 0)
    print(min_count)
    print(cache_list)

    print(count_of_coin2())