#思路： 此题的要求是O(1)的额外空间，直接对原数组进行修改，所以涉及到删除数组元素。在python中删除数组元素使用pop或者del等会导致索引变化，导致
#index out of range报错，一般通用的办法是采用倒序循环
#参见这篇文章https://www.cnblogs.com/bananaplan/p/remove-listitem-while-iterating.html
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        #从最后一个开始
        ret = [nums[-1]]
        #倒序遍历 从倒数第二个到第一个，如果正序遍历会报错因为删除元素之后list变小了但是遍历的i还是按照原来的list大小来的
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == ret[-1]:
                nums.pop(i)
            if  nums[i] != ret[-1]:
                ret.append(nums[i])
                
        return len(nums)
