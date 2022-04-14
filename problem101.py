# <---coding: utf-8--->
# @Time:  2021/12/24/23:09
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.theSame(root.right, root.left)

    def theSame(self, right: TreeNode, left: TreeNode) -> bool:
        if right is None and left is None:
            return True
        elif right is None or left is None or right.val != left.val:
            return False
        else:
            return self.theSame(right.right, left.left) and self.theSame(right.left, left.right)
