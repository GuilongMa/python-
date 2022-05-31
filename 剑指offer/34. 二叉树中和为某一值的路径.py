# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        if not root:
            return []
        nums_list = []
        cur_list = [root.val]

        def bfs(cur_sum, node, cur_list):
            if not node.left and not node.right:
                if cur_sum == sum and cur_list:
                    nums_list.append(cur_list)
                return nums_list
            if node.left:
                bfs(cur_sum + node.left.val, node.left, cur_list + [node.left.val])
            if node.right:
                bfs(cur_sum + node.right.val, node.right, cur_list + [node.right.val])

        bfs(root.val, root, cur_list)
        return nums_list