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
            	#需要判断res是否为空，如果先出现右括号
                if not res or res[-1] != keymap[i]:
                    return False
                else:
                    res.pop()
        if not res:
            return True
        return False