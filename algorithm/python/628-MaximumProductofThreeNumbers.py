#思路：分几种情况考虑，三个数的正负情况，三正，三负，两正一负，两负一正，含0
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #先对数组按从小到大排序
        nums.sort()
        #三正 三负 两正一负 一正两负
        res = []
        #如果三正或者三负，都是最大的三个数的乘积
        max1 = nums[-3] * nums[-2] * nums[-1]
        res.append(max1)
        for i in range(len(nums)):
            if nums[i] < 0 and nums[i]>=0:
                num1 = nums[i]
                #如果是两正一负，则结果是负数，此时用最小的负数
                max2 = nums[-1] * nums[-2] * num1
                res.append(max2)
        #如果是两负一正，结果是正，此时用最小的负
        max3 = nums[-1] * nums[0] * nums[1]
        res.append(max3)
        if 0 in nums:
            res.append(0)
        return max(res)