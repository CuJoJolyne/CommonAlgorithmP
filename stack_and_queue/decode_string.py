#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os


# https://leetcode-cn.com/problems/decode-string/
def decode_string(src):
    stack = []
    for c in src:
        #print(c)
        if c == ']':
            # 获取右括号左方第一个需要提取的子串
            tempCharList = []
            while (stack[-1] != '['):
                tempCharList.append(stack.pop(-1))
            #print(tempStr)
            # 弹出'['
            stack.pop(-1)
            # 先获取数字占了几个字符
            numCount = 0
            while (numCount < len(stack) and stack[-1-numCount] >= '0' and stack[-1-numCount] <= '9'):
                numCount += 1
            # 提取数字倍数
            numStr = ""
            for i in range(numCount, 0, -1):
                #print(i)
                numStr += stack.pop(-1-i+1)
            #print(numStr)
            # 把这次提取出的 数字[多个字符] 转换成展开的纯字符形式，再压入栈中（因为可能有括号嵌套，如例2）
            for i in range(int(numStr)):
                for j in range(len(tempCharList)-1, -1, -1):
                    stack.append(tempCharList[j])
        else:
            stack.append(c)
    result = ""
    for i in range(len(stack)):
        result += stack[i]
    print(result)

if __name__=='__main__':
    decode_string("10[a]002[bc]")
    decode_string("3[a2[c]]")