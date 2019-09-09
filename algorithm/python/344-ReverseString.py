#思路：因为要求不使用额外空间，故使用异或进行交换，首尾互换，依次前进，到中间截止
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while(i<j):
            a = ord(s[i])
            b = ord(s[j])
            a = a^b
            b = a^b
            a = a^b
            s[i] = chr(a)
            s[j] = chr(b)
            i+=1
            j-=1