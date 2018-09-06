#思路：本题颇费了一番时间，主要是因为提交总是timeout超时，参见注释为第一版写法.分析应该是因为太多sum()函数的调用导致超时
#      经过参考和思考，绝对使用累加和累减来获取每次的左右子数组之和，这种方式比每次都sum好得多，整体只需要sum一次，如此
#	   更改之后便不再超时，需多多借鉴此种写法
#基本思路：遍历数组，对每个元素做中心索引时的左右元素之和作比较，如果相同则返回index
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                leftSum = 0
                rightSum = total - nums[i]
            else:
                leftSum += nums[i-1]
                rightSum -= nums[i]
            if leftSum == rightSum:
                return i
        return -1

    # def pivotIndex(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if len(nums) == 1:
    #         return 0
    #     for i in range(len(nums)):
    #         if i == 0:
    #             leftSum = 0
    #         else:
    #             leftSum = sum(nums[:i])
    #         rightSum = sum(nums[i+1:])
    #         if leftSum == rightSum:
    #             return i
    #     return -1