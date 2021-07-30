# 思路：简单的ascii码转换
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        le = len(columnTitle)
        res = 0
        for i in columnTitle:
            num = ord(i) - 64
            res += pow(26, le-1) * num
            le -= 1
        return res