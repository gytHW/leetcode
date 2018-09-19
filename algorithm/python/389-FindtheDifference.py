#思路：简单的遍历t，不在s中直接返回值，在s中则删去s中此元素，到最后s空了，t中剩下的就是所求
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sl = list(s)
        tl = list(t)
        for i in range(len(tl)):
            sslice = sl[:]
            if tl[i] not in sslice:
                return tl[i]
            if tl[i] in sslice:
                sl.remove(tl[i])