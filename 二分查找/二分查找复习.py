def binary_search(num_list, num):
    if not num_list:
        return -1
    length = len(num_list)
    left = 0
    right = length - 1
    while left <= right:
        middle = (left + right) // 2
        if num_list[middle] == num:
            return middle
        elif num_list[middle] > num:
            right = middle - 1
        else:
            left = middle + 1
    return -1


# 递归实现
def b_search(num_list, target):
    return b_search_internally(num_list, 0, len(num_list)-1, target)


def b_search_internally(num_list, low, high, target):
    if low > high:
        return -1

    mid = low+int((high-low) >> 2)
    if num_list[mid] == target:
        return mid
    elif num_list[mid] < target:
        return b_search_internally(num_list, mid+1, high, target)
    else:
        return b_search_internally(num_list, low, mid-1, target)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    num = 3
    print(binary_search(nums, num))
    print(b_search(nums, num))

    nums = [8]
    num = 3
    print(binary_search(nums, num))
    print(b_search(nums, num))
