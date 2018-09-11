class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        line = 0
        num = 0
        while( num <= n):
            num += line + 1
            line += 1
        return line - 1 #完整行数