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
            length = len(q)
            num_lst = []
            while length:
                node = q.popleft()
                num_lst.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                length -= 1
            if num_lst:
                print_list.append(num_lst)
        return print_list
