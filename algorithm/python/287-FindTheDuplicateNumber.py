#思路：这题属于想太多，因为太在意额外空间O(1)的要求，想另辟蹊径用二分法查找，反而浪费了很多时间，其实简单的用set去重就可以了
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set()
        for i in range(len(nums)):
            if nums[i] in res:
                return nums[i]
            res.add(nums[i])
        # nums.sort()
        # if len(nums) == 2:
        #     print(nums[0])
        #     return
        # if len(nums) == 3:
        #     if nums[len(nums) // 2] == nums[0]:
        #         print(nums[0])
        #         return
        #     else:
        #         print(nums[-1])
        #         return
        # length = len(nums)
        # mid = nums[length // 2]
        # n = length - 1
        # if mid <= n // 2:
        #     self.findDuplicate(nums[:(length//2 + 1)])
        # if mid > n //2:
        #     self.findDuplicate(nums[(length//2 - 1):])