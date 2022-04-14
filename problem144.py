# <---coding: utf-8--->
# @Time:  2022/1/1/21:42
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = list()
        preorder(root)
        return res
