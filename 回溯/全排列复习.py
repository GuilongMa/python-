import copy


def permutation(nums, count, k):
    if k == 1:
        new_nums.append(copy.deepcopy(nums))

    for i in range(k):
        nums[i], nums[k-1] = nums[k-1], nums[i]

        permutation(nums, count, k - 1)

        nums[i], nums[k-1] = nums[k-1], nums[i]


def permute(nums):

    def dfs(path):
        if len(path) == size1:
            res.append(path[:])
            return
        for depth in range(size1):
            if not used[depth]:
                path.append(nums[depth])
                used[depth] = True
                dfs(path)
                used[depth] = False
                path.pop()

    size1 = len(nums)
    if size1 == 0:
        return []
    used = [False for i in range(size1)]
    res = []
    dfs([])
    return res


def permute2(nums):

    def dfs(first):
        if first == size1:
            res.append(nums[:])
            return
        for i in range(first, size1):
            nums[i], nums[first] = nums[first], nums[i]
            dfs(first+1)
            nums[first], nums[i] = nums[i], nums[first]

    size1 = len(nums)
    if size1 == 0:
        return []
    res = []
    dfs(0)
    return res


if __name__ == "__main__":
    num_list = [1, 2, 3]
    # ①
    # new_nums = []
    # size = len(num_list)
    # end = size
    # permutation(num_list, size, end)
    # print(new_nums)
    print(permute(num_list))


