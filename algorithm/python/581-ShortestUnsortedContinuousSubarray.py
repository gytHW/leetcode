# 思路：排序，之后对比排序的数组和未排序的数组，如果元素在应该在的位置上说明无需排序，两端推进获得两个边界
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        sorted_nums = sorted(nums)
        while start <= end and nums[start] == sorted_nums[start]:
            start += 1
        while start <= end and nums[end] == sorted_nums[end]:
            end -= 1
        return end - start + 1