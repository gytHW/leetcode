#思路： 二叉树层序遍历，经典思路是采用BFS广度优先遍历，而bfs就是要引入一个deque队列，按层入队出队。
# python如何创建一个队列？deque
#  from collections import deque
#  q = deque()
#  这里没有使用deque 而是用list代替，相应出队的时候就是pop(0)
#  如果是deque的话，出队就是node = queue.popleft()
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while len(queue) > 0:
            tmp = []
            for _ in range(len(queue)):  #遍历这一层的节点
                node = queue.pop(0) #因为这里用的是list代替deque
                tmp.append(node.val)
                if node.left:  #将下一层的节点入队
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res