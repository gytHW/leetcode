#思路：这题很简单，看看糖果总共多少种，少于一般就获取全部种类，最多获取一半
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        uniqueCandies = set(candies)
        num = len(list(uniqueCandies))
        half = len(candies) // 2 
        if num <= half:
            return num
        else:
            return half