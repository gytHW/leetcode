#思路：很简单一道题，lc的每日一题，没什么好说的
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxChild = max(candies)
        res = []
        for i in candies:
            res.append(False) if i+extraCandies < maxChild else res.append(True)
        return res