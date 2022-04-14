# <---coding: utf-8--->
# @Time:  2022/1/1/21:53
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)
        ans = []
        postorder(root)
        return ans