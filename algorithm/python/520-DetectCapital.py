#思路：本题要处理三种情况 全大写 全小写 首字母大写其余小写
import re

class Solution:
    def detectCapitalUse(self, word):
    	# | 表示“或” 左边或者右边的表达式
    	# []表示匹配一个，*表示匹配0次或多次，两者配合[A-Z]*表示匹配多个大写字母，
    	# 为防止后面出现小写字母，加上一个结尾符号$,即表示直到结尾全大写
        match = re.match('([A-Z]*$)|([a-z]*$)', word)
        if match:
            return True
            #此正则 ^表示开头，中括号匹配一个，所以^[A-Z]表示以一个大写字母开头，
            #参照上面的注释,[a-z]*$表示匹配多小写字母到结尾，这个表达式整体就表示大写字母开头后面全小写
        elif(len(word) > 1 and re.match('^[A-Z][a-z]*$', word)):
            return True
        return False