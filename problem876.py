# <---coding: utf-8--->
# @Time:  2022/5/8/1:01
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node1 = node2 = head
        while node2 and node2.next:
            node1 = node1.next
            node2 = node2.next.next
        return node1
