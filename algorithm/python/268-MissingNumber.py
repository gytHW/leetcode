#思路：类似于另一个“数组中只出现过一次的数字”的问题，可以用异或来解决，让这个数组的每个元素异或不缺数的完整数组中的每个元素，
#因为A^A=0, 0^A=A，异或又满足结合律。所以最后所有相同的数字成对抵消等于0，剩余的那个数字就是所求的数字
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i] ^ (i+1)
        return res