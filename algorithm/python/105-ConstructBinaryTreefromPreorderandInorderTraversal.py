#思路：二叉树的问题基本都可以用递归来解。
# 根据前序遍历可以确定根节点，一定是第一个元素。找到根节点在终须遍历的位置，就能得到左右子树。同理可以确定前序遍历的左右子树。
# 从而递归求解
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:rootIndex+1], inorder[:rootIndex])
        root.right = self.buildTree(preorder[rootIndex+1:], inorder[rootIndex+1:])
        return root