"""将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0

+2147483647
1a33

2147483647
0
"""
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s=='' or s=='+' or s=='-':
            return 0

        list_right=['+','-','0','1','2','3','4','5','6','7','8','9']
        if s[0] not in list_right:
            return 0

        for i in s[1:]:
            if i not in list_right[2:]:
                return 0

        if s[0]=='+':
            return eval(s[1:])
        elif s[0]=='-':
            return eval('-'+s[1:])
        elif s[0] in list_right[2:]:
            return eval(s)

s=Solution()
print(type(s.StrToInt('+')))
print(s.StrToInt('+'))
