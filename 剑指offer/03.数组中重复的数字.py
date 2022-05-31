class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        return -1

    def findRepeatNumber_2(self, nums: [int]) -> int:
        num_set = set()
        for i in nums:
            if i in num_set:
                return i
            num_set.add(i)


if __name__ == "__main__":
    array = [2, 3, 1, 0, 2, 5, 3]
    sol = Solution()
    print(sol.findRepeatNumber(array))
