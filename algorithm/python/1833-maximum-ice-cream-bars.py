# 思路：简单的贪心算法，优先最便宜的可以数量最多

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        maxnum = 0
        for i in costs:
            if coins-i>=0:
                maxnum = maxnum+1
                coins = coins-i
            else:
                return maxnum
        return maxnum