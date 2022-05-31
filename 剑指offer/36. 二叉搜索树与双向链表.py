"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        self.prev = None
        self.inorder(root)
        self.head.left, self.prev.right = self.prev, self.head
        return self.head

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        if self.prev:
            self.prev.right, node.left = node, self.prev
        else:
            self.head = node
        self.prev = node
        self.inorder(node.right)

