import random


# 原地排序，时间复杂度为O(nlogn),原因：递归logn层，每层对分区函数的多次调用中的遍历元素个数总和都为n，故总的遍历次数为nlogn
def quick_sort(num_list, left, right):
    # 边界
    if left >= right:
        return
    # 分区函数
    mid = partition(num_list, left, right)
    # 使用递归技巧编写
    quick_sort(num_list, left, mid - 1)
    quick_sort(num_list, mid + 1, right)


# 采用单边循环法
def partition(num_list, left, right):
    # 随机函数获取pivot数值
    pivot_index = random.randint(left, right)
    pivot_value = num_list[pivot_index]
    # 交换pivot_index和right两个位置的数值，即将pivot数值放到需要分区的切片的最末尾，为了分区方便
    num_list[pivot_index], num_list[right] = num_list[right], num_list[pivot_index]
    i = left
    # 遍历比较，i位置的前面为大于pivot数值的元素
    for j in range(left, right):
        if num_list[j] > pivot_value:
            num_list[i], num_list[j] = num_list[j], num_list[i]
            i += 1
    # 将pivot值放到分区位置
    num_list[i], num_list[right] = num_list[right], num_list[i]
    return i


def quick_sort2(nums, left, right):
    if left >= right:
        return
    mid = partition1(nums, left, right)
    quick_sort2(nums, left, mid-1)
    quick_sort2(nums, mid+1, right)


def partition1(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i


if __name__ == "__main__":
    # nums = [52, 11, 10, 6, -1, 2.2, 8, 8, 15]
    L = 0
    nums = [52, 15, 11, 10, 8, 8, 6, 2.2, -1]
    R = len(nums) - 1
    # quick_sort(nums, L, R)
    # print(nums)
    quick_sort2(nums, L, R)
    print(nums)
