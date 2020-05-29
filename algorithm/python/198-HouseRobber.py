# 思路：求最值一般考虑用动态规划。这里考虑，如果要偷n家，分偷第n家和不偷第n家两种情况。如果偷第n家，那就不偷第n-1家，总金额就是偷前n-2家
# 最大金额加上第n家。如果不偷第n家，那就等同于偷前n-1家的最大金额。两者取最大值就是。
# dp转移方程：dp[n] = max(dp[n-1], dp[n-2]+nums[n])
# 要注意，一般推荐从底向上的计算方式。
# 参考https://leetcode-cn.com/problems/house-robber/solution/dong-tai-gui-hua-jie-ti-si-bu-zou-xiang-jie-cjavap/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        L = len(nums)
        dp = [0]*(L+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, L+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        return dp[L]