# <---coding: utf-8--->
# @Time:  2021/12/25/23:42
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
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def MaxHeight(root: TreeNode) -> int:
            if not root:
                return 0
            else:
                return max(MaxHeight(root.left), MaxHeight(root.right)) + 1

        def MinHeight(root: TreeNode) -> int:
            if not root:
                return 0
            else:
                return min(MinHeight(root.left), MinHeight(root.right)) + 1

        if MaxHeight(root) - MinHeight(root) > 1:
            return False
        return True
