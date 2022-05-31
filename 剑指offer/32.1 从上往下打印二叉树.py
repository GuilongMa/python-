# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> [int]:
        print_list = []
        if not root:
            return print_list
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            print_list.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return print_list
