class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [n for n in nums if n%2 != 0] + [n for n in nums if n%2 == 0]