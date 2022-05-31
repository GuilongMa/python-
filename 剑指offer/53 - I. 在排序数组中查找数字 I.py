class Solution:
    def search(self, nums: [int], target: int) -> int:

        def get_first_equal_value(nums, n, value):
            left = 0
            right = n - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if value < nums[mid]:
                    right = mid - 1
                elif value > nums[mid]:
                    left = mid + 1
                else:
                    if mid == 0 or nums[mid - 1] < value:
                        return mid
                    right = mid - 1
            return None

        def get_last_equal_value(nums, n, value):
            left = 0
            right = n - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if value < nums[mid]:
                    right = mid - 1
                elif value > nums[mid]:
                    left = mid + 1
                else:
                    if mid == n - 1 or nums[mid + 1] > value:
                        return mid
                    left = mid + 1
            return None

        n = len(nums)
        first = get_first_equal_value(nums, n, target)
        last = get_last_equal_value(nums, n, target)
        if first == None:
            return 0
        else:
            return last - first + 1

class Solution2:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if tar <= nums[m]: j = m - 1
                else: i = m + 1
            return i
        return helper(target+1) - helper(target)

class Solution3:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar: i = m + 1
                else: j = m - 1
            return i
        return helper(target) - helper(target - 1)