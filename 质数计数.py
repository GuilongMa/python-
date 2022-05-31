def prime_count(m):
    flag_list1 = [1 for i in range(0, m+1)]
    c = 0
    for i in range(2, m+1):
        if flag_list1[i] == 1:
            c += 1
        j = i * i
        while j < m+1:
            flag_list1[j] = 0
            j += i
    flag = False
    if flag_list1[m] == 1:
        flag = True
    return c, flag


if __name__ == "__main__":
    m = 10
    n = 20
    c1, flag1 = prime_count(m)
    c2, _ = prime_count(n)
    print(c1, c2)
    if flag1:
        print(c2 - c1 + 1)
    else:
        print(c2 - c1)


