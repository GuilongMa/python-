def erfen_check(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if value < L[mid]:
            right = mid - 1
        elif value > L[mid]:
            left = mid + 1
        else:
            return mid
    return None


def get_first_equal_value(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if value < L[mid]:
            right = mid - 1
        elif value > L[mid]:
            left = mid + 1
        else:
            if mid == 0 or L[mid - 1] < value:
                return mid
            right = mid - 1
    return None


def get_first_equal_value2(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if value <= L[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if left < n and L[left] == value:
        return left
    return None


def get_last_equal_value(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if value < L[mid]:
            right = mid - 1
        elif value > L[mid]:
            left = mid + 1
        else:
            if mid == n - 1 or L[mid + 1] > value:
                return mid
            left = mid + 1
    return None


def get_last_equal_value2(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if L[mid] <= value:
            left = mid + 1
        else:
            right = mid - 1
    if right < n and L[right] == value:
        return right
    return None


def get_first_large_equal_value(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if value <= L[mid]:
            if mid == 0 or L[mid - 1] < value:
                return mid
            right = mid - 1
        else:
            left = mid + 1
    return None


def get_first_large_equal_value2(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if value <= L[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if left < n and L[left] >= value:
        return left
    return None


def get_last_small_equal_value(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if value >= L[mid]:
            if mid == n - 1 or L[mid + 1] > value:
                return mid
            left = mid + 1
        else:
            right = mid - 1
    return None


def get_last_small_equal_value2(L, n, value):
    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if value >= L[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if right > -1 and L[right] <= value:
        return right
    return None


if __name__ == "__main__":
    L = [1, 2, 3, 5, 6, 7, 9]
    L1 = [1, 2, 4, 5, 7, 7, 8, 9]
    # print(erfen_check(L, 7, 4))
    print(get_first_equal_value([1], 1, 1))
    print(get_last_equal_value(L1, 8, 3))
    print(get_first_large_equal_value(L1, 8, 6))
    print(get_last_small_equal_value(L1, 8, 7))

    print(get_first_equal_value2([1], 1, 1))
    print(get_last_equal_value2(L1, 8, 3))
    print(get_first_large_equal_value2(L1, 8, 6))
    print(get_last_small_equal_value2(L1, 8, 7))
    import bisect