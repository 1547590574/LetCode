# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []
        cur = root
        # 迭代的中序遍历 ，先拿到最左子树，然后左 -> 中 -> 右
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur=cur.right
        return ans