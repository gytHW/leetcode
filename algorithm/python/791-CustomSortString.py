#思路：先把T中有的S中出现的字符全拿出来，最后再把T剩余的元素添到后面，需注意的是，S中每个元素都可能在T中出现多次
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s = list(S)
        t = list(T)
        ret = []
        for i in range(len(s)):
        	#重点 这里需要用t的切片进行循环而不是t，否则即使t去掉之后下次循环的对象仍然是原来的t，达不到去掉已找到元素的效果
            while s[i] in t[:]:
                k = t.index(s[i])
                ret.append(s[i])
                #这里需用remove而不是pop
                t.remove(s[i])
        ret.append(''.join(t))
        return ''.join(ret)