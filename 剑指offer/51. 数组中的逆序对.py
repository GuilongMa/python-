class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, nums: [int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)


class Solution2:
    def reversePairs(self, nums: [int]) -> int:
        self.c = 0
        self.temp = [0] * len(nums)

        def merge(left, mid, right, nums):
            i, j = left, mid+1
            k = left
            while i <= mid  or j <= right:
                if i > mid:
                    self.temp[k] = nums[j]
                    j += 1
                elif j > right:
                    self.temp[k] = nums[i]
                    i += 1
                elif nums[i] <= nums[j]:
                    self.temp[k] = nums[i]
                    i += 1
                else:
                    self.temp[k] = nums[j]
                    self.c += mid - i + 1
                    j += 1
                k += 1

            for k in range(left, right+1):
                nums[k] = self.temp[k]


        def merge_sort(left, right, nums):
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort(left, mid, nums)
            merge_sort(mid + 1, right, nums)
            merge(left, mid, right, nums)

        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        merge_sort(start, end, nums)
        return self.c
