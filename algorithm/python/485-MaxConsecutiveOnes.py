#思路：遍历数组，用count记录遇到的1的个数，如果遇到0就用list记下这一段元素中1的个数，清零count，最后比较这么多段中哪段的count最大
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0:
                res.append(count)
                count = 0
            res.append(count) #特殊情况，全是1没有0
        return max(res)