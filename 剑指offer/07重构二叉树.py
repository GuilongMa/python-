# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        inorder_index_list = {}
        for i in range(len(inorder)):
            inorder_index_list[inorder[i]] = i

        return self.reConstructBinaryTree(inorder_index_list, preorder, 0, len(preorder) - 1, 0)

    def reConstructBinaryTree(self, inorder_index_list, preorder, pre_l, pre_r, in_l):
        if pre_l > pre_r:
            return
        root = TreeNode(preorder[pre_l])
        in_index = inorder_index_list.get(root.val)
        leftTreeSize = in_index - in_l
        root.left = self.reConstructBinaryTree(inorder_index_list, preorder, pre_l + 1, pre_l + leftTreeSize, in_l)
        root.right = self.reConstructBinaryTree(inorder_index_list, preorder, pre_l + leftTreeSize + 1, pre_r,
                                                in_l + leftTreeSize + 1)
        return root