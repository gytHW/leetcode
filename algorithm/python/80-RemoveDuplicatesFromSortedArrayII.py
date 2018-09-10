#思路：这题有些可说的，这题是26题删除数组重复项的进阶变种，需要加个count参数判断次数即可，但是有很多小问题需要注意，比如说continue的添加，count数目的判断，
# count = count +1 与count += count的区别
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        ret = [nums[-1]]
        count = 1
        for i in range(len(nums)-2, -1, -1):
            # print('ret' + str(ret[-1]))
            # print('num' + str(nums[i]))
            # print('count' + str(count))
            # print('------------------')
            if nums[i] == ret[-1] and count == 2:
                nums.pop(i)
                #continue不可少，否则这里count操作完之后可能会继续走下面的第三个判断，这是一个隐藏的bug需注意
                continue
            if  nums[i] != ret[-1]:
                ret.append(nums[i])
                count = 1
                continue
            if nums[i] == ret[-1] and count < 2:
            	#这里需注意，不能用count += count 这个和count = count + 1是不一样的，需要注意
                count = count + 1 
                ret.append(nums[i])
                continue
        # print(ret)
        return len(nums)