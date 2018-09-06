#思路：用一个set去重，如果去重后少于三个元素，说明不存在第三大的数，否则把这个set赋给一个list进行排序，第三大的数即为原数组中第三大的数
#      需注意本题要求时间复杂度O(n)
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #如果数组元素少于三个，那肯定不存在第三大的数，直接返回最大数
        if len(nums) < 3:
            return max(nums)
        num_set = set(nums) #用set去重
        if len(num_set) < 3:
            return max(nums)
        else:
            res = list(num_set)
            res.sort()
            return res[len(res)-3]