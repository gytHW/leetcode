#思路： 最基本的二分查找算法，需要注意的是mid下标的确定应该用left + right，这里需仔细体会
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2 #这里的left + right是核心关键，如果是right - left的话就是对每个二分的小数组取中值下标了
            midnum = nums[mid]
            if target == midnum:
                return mid
            elif target < midnum:
                right = mid - 1
            else:
                left = mid + 1
        return -1