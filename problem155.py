# <---coding: utf-8--->
# @Time:  2022/1/1/21:54
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import math


class MinStack:
    def __init__(self):
        self.ans = []
        self.minstack = [math.inf]
    def push(self, val: int) -> None:
        self.ans.append(val)
        self.minstack.append(min(val,self.minstack[-1]))
    def pop(self) -> None:
        self.ans.pop()
        self.minstack.pop()
    def top(self) -> int:
        return self.ans[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
# 上面实现到是实现了，只是太慢了  580ms不能接受,改进后用一个多余的数组记录最小值，最小的一定在其最上面，也就是-1位，前面都是历史最小值

