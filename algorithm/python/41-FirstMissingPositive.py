#思路：本题难点在于各种边际条件的判断，[],[2],[-1,-2,-3]等情况都需要考虑到
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: #空数组
            return 1
        flag = max(nums)
        if flag <= 0: #无正整数的数组
            return 1
        #遍历1到n之间的自然数，找到未出现的最小数
        for i in range(1, len(nums)+1): #单元素数组
            if i not in nums:
                return i
        #如果未遍历到，说明未出现的最小数比数组最大值还大，则返回最大值+1的自然数
        return flag + 1