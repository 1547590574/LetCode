# <---coding: utf-8--->
# @Time:  2021/12/25/10:51
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 只击败30%的人，所以决定改进一下时间复杂度，想在添加temp时就判断增减顺序或者奇偶性。
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        result = []
        cur, end = 0, 1
        level = -1
        result.append(root)
        while cur < len(result):
            mod = 0
            level += 1
            temp = []
            end = len(result)
            while cur < end:
                print(result[cur].val, end=' ')
                temp.append(result[cur].val)
                if result[cur].left:
                    result.append(result[cur].left)
                if result[cur].right:
                    result.append(result[cur].right)
                cur += 1
            print("层数:", level, end=' ')
            print()
            mod = level % 2
            if mod == 0:
                i = 0
                if temp[-1] % 2 != 1:
                    return False
                while i < len(temp) - 1:
                    if temp[i] % 2 != 1:
                        return False
                    if temp[i] >= temp[i + 1]:
                        return False
                    i += 1
            if mod == 1:
                i = 0
                if temp[-1] % 2 != 0:
                    return False
                while i < len(temp) - 1:
                    if temp[i] % 2 != 0:
                        return False
                    if temp[i] <= temp[i + 1]:
                        return False
                    i += 1
        return True



#方法二是官方解法，用的时层次遍历
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev = float('inf') if level % 2 else 0
            nxt = []
            for node in queue:
                val = node.val
                if val % 2 == level % 2 or level % 2 == 0 and val <= prev or level % 2 == 1 and val >= prev:
                    return False
                prev = val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            level += 1
        return True
