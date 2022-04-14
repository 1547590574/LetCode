# <---coding: utf-8--->
# @Time:  2021/12/26/0:25
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.right is None or root.left is None:
            return max(self.minDepth(root.left) ,self.minDepth(root.right)) + 1
        else:
            return 1 + max(self.minDepth(root.left),self.minDepth(root.right))
