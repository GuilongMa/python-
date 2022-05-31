# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:16:38 2018

@author: qzxy
"""
from typing import List


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: 
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for temp_list in self.permute(n):
                ans.append([num] + temp_list)
                print(ans)
            print('-----End-----')
        return ans


class Solution2:
    @staticmethod
    def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


# 标记数组
class Solution3:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        def dfs(depth, path):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(depth + 1, path)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(0, [])
        return res


# 包含重复元素
class Solution4(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        ans = []
        mark_dict = {}
        for i, num in enumerate(nums):
            if not mark_dict.get(num):
                mark_dict[num] = True
                n = nums[:i] + nums[i+1:]
                for temp_list in self.permute(n):
                    ans.append([num] + temp_list)
        return ans


if __name__ == "__main__":
    sol = Solution4()
    num_list = [1, 1, 2]
    print(sol.permute(num_list))
