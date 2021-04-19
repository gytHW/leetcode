# 思路：一开始想着从数学定义上去解决，找对角线元素，写起来很繁琐麻烦。后来看题解得到启发，
# 其实只需要对比每个元素和他右下角的元素是否相等就行
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for x in range(rows-1):
            for y in range(cols-1):
                if matrix[x][y] != matrix[x+1][y+1]:
                    return False
        return True

