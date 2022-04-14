# <---coding: utf-8--->
# @Time:  2021/12/25/23:37
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二分法查找的结果就为二叉搜索树，此时考虑的是节点左边还是节点右边的点作为当前节点的左节点还是右节点，
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper((0, len(nums) - 1))
