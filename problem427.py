# <---coding: utf-8--->
# @Time:  2022/4/29/23:40
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# Definition for a QuadTree node.
from typing import List

# 这里定义的四叉树是在方针中定义的，首先建立两条分割线，水平和竖直的，一个区域所有方格的值一样 就可以认为是一个叶子节点
# 叶子节点的值为该区域的值（1和0）两种情况，如此类推，直至区域中所有格子的值一样。
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # 这里用一个内部的方法，if中的语句用以构建叶子节点，else中的语句构建递归语句。
        # 同时第一次接触方法返回值为自定义方法的。 加上引号即可。
        def dfs(r0: int, c0: int, r1: int, c1: int) -> 'Node':
            if all(grid[i][j] == grid[r0][c0] for i in range(r0, r1) for j in range(c0, c1)):
                return Node(grid[r0][c0] == 1, True)
            return Node(
                True,
                False,
                dfs(r0, c0, (r0 + r1) // 2, (c0 + c1) // 2),
                dfs(r0, (c0 + c1) // 2, (r0 + r1) // 2, c1),
                dfs((r0 + r1) // 2, c0, r1, (c0 + c1) // 2),
                dfs((r0 + r1) // 2, (c0 + c1) // 2, r1, c1),
            )
        # 这里四个dfs很完美，四个分割就行。
        return dfs(0, 0, len(grid), len(grid))
