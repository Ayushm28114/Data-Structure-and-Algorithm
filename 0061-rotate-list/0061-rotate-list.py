# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        i = head

        while i.next:
            length += 1
            i = i.next

        m = k % length

        j = head
        i = head

        while m:
            j = j.next
            m -= 1
        
        while j.next:
            j=j.next
            i=i.next
        
        j.next = head
        p = i.next
        i.next = None
        return p
