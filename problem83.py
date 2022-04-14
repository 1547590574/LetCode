class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        current = head.next
        past = head
        while current:
            if current.val == past.val:
                past.next = current.next
            current = current.next
            past = past.next
        return head
