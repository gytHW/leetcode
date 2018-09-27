#思路：栈的简单运用，左括号入栈，右括号如果匹配则出栈
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        left = ("(", "[", "{")
        right = (")", "]", "}")
        keymap = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in left:
                res.append(i)
            if i in right:
            	#这个判断比较重要，如果先出现右括号
                if not res:
                    return False
                last = res[-1]
                if last == keymap[i]:
                    res.pop()
                else:
                    return False
        if not res:
            return True
        return False