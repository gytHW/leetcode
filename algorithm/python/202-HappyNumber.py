#思路：这道题的核心是拆分数字和判断怎么算无限循环

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set() #用set保存已经出现过的数字，如果再次出现，则说明无限循环了，不是快乐数
        while True:
            seen.add(n)
            n = self.sumSquare(n)
            if n == 1:
                return True
            elif n in seen:
                return False
        
    # 借鉴了一种新的求各位数字的方法        
    def sumSquare(self, n):
        sum = 0
        while n != 0:
            tmp = n % 10
            sum += pow(tmp, 2)
            n = (n - tmp) / 10
        return sum