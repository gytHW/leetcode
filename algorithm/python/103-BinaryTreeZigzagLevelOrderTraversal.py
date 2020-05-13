#思路：这题和上一题102题的思路一致，只需要在输出的时候对偶数行反转下就行
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        count = 1 #记录层数
        while len(queue) > 0:
            tmp = []
            for _ in range(len(queue)):  #遍历这一层的节点
                node = queue.pop(0) #因为这里用的是list代替deque
                tmp.append(node.val)                
                if node.left:  #将下一层的节点入队
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #输出的时候对偶数层反转下（假设根节点为第一层）
            if count % 2 == 0:
                tmp.reverse()
            count += 1
            res.append(tmp)
        return res