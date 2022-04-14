from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 这个参考了一下评论区的想法，原本想先将两个链表做链接，然后冒泡排序，但是忘记怎么写了，然后根据以空间换时间的想法，新建一个链表作为合并后的新链表，由于要保存表头，所以用current指针索引
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        linkHead = ListNode()
        current = linkHead
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        if list1 is None:
            current.next = list2
        else:
            current.next = list1
        return linkHead.next
