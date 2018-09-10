#思路：注意几种特殊情况其实可以合并简化代码，比如在范围中和超出最大，其实都是返回i+1
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target == nums[i] or target < nums[i]:
                return i
        return i+1