# <---coding: utf-8--->
# @Time:  2022/1/1/23:13
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 走到尽头见不到你，于是走过你来时的路，等到相遇时才发现，你也走过我来时的路。
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA
