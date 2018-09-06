#思路：本题很简单，遍历数组，用一个set出现过的数，如果再次出现就说明出现了两次
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        record = set()
        res = []
        for i in range(0, len(nums)):
        	#set添加元素用add，list添加元素用append
            if nums[i] not in record:
                record.add(nums[i])
            else:
                res.append(nums[i])
        return res