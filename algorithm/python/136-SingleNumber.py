#思路：运用异或的性质，任何数异或自身等于0，任何数异或0等于自身。所以把所有元素异或运算，最后剩下的就是那个没有成对的单独元素
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res