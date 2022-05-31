# 取最小值
def xunazhuan_array(List):
    # 无重复元素，比如[3, 4, 1, 2]
    low = 0
    high = len(List) - 1
    while low < high:
        mid = low + (high - low) // 2
        if List[mid] <= List[high]:
            high = mid
        else:
            low = mid + 1

    return List[low]


if __name__ == "__main__":
    List = [4, 5, 1, 2, 3]
    print(xunazhuan_array(List))
