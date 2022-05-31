def xi_er_sort(L):
    if len(L) == 1:
        return
    length = len(L)
    gap = 1
    while gap < length // 3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, length):
            j = i-gap
            temp = L[i]
            while j >= 0 and L[j] > temp:
                L[j+gap] = L[j]
                j -= gap
            L[j+gap] = temp
        gap = gap // 3
    return L


if __name__ == "__main__":
    L1 = [1,2,2,4,3]
    L2 = [4,3,2,6,5,8,7,9,1]
    print(xi_er_sort(L1))
    print(xi_er_sort(L2))