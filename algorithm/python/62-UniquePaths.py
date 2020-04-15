class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 思路：参照https://www.zhihu.com/question/23995189/answer/1094101149，这题使用动态规划（DP）解决。
        # 那我们就定义 dp[i] [j]的含义为：当机器人从左上角走到(i, j) 这个位置时，一共有 dp[i] [j] 种路径。
        # 那么，dp[m-1] [n-1] 就是我们要的答案了。
        # 想象以下，机器人要怎么样才能到达 (i, j) 这个位置？由于机器人可以向下走或者向右走，
        # 所以有两种方式到达一种是从 (i-1, j) 这个位置走一步到达一种是从(i, j - 1) 这个位置走一步到达
        # 因为是计算所有可能的步骤，所以是把所有可能走的路径都加起来，所以关系式是 dp[i] [j] = dp[i-1] [j] + dp[i] [j-1]。

        #注意python定义二维list的方法，这里是生成一个全为空值None的m x n list
        dp = [[None for i in range(n)] for i in range(m)]
        if m <= 0 or n <= 0:
            return 0
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]