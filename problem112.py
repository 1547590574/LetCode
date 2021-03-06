# <---coding: utf-8--->
# @Time:  2021/12/31/10:54
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
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum -= root.val
        if root.right is None and root.left is None:
            return targetSum == 0
        return self.hasPathSum(root.right,targetSum) or self.hasPathSum(root.left,targetSum)