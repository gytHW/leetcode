# 思路：构造一个字典映射，模式作为key 对应的值为value，一一对应就可以判断是否符合模式了
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split( )
        pattern_dict = {}
        if len(pattern) != len(slist):
            return False
        for index,v in enumerate(pattern):
            if v not in pattern_dict:
                # “abbac”和"cat dog dog cat pig"
                if slist[index] in pattern_dict.values():
                    return False
                else:
                    pattern_dict[v] = slist[index]
                continue
            if pattern_dict[v] != slist[index]:
                return False
        return True