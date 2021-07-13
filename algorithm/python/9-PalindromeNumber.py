# 思路：头尾逐一对比直到相遇
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        i = 0
        j = len(y)-1
        while i < j:
            if y[i] != y[j]:
                return False
            i = i+1
            j = j-1
        return True