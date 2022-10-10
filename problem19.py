# <---coding: utf-8--->
# @Time:  2022/5/8/1:06
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 构造一个头部节点会方便很多
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0,head)
        slow = dummy
        fast = head
        for i in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next= slow.next.next
        return dummy.next

