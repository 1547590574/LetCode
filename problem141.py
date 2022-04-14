# <---coding: utf-8--->
# @Time:  2022/1/1/21:31
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针，以前看到过，一个一次走两步，一个一次走一步，如果有环，慢的一定会被快的追上，此时发生套圈了，但不一定是套一圈。
# 还有一种做法是hash表，弄个set  每次把val加入里面，有重复就意味着有环。 这里要知道跳出条件，就是没有环，走到底就会返回False。

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast, slow = head.next, head
        while slow != fast:
            if not slow or not fast:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
