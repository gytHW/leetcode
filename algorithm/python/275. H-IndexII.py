# 思路：升序排列，只需从最后一个开始比，最后一个大于1，倒数第二个大于2，倒数第三个大于3...
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        le = len(citations)
        h = 0
        for i in range(le):
            if citations[le-i-1] >= h+1:
                h = h+1
        return h