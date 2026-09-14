# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            head=None
            return head
        
        dummy=ListNode(-1)
        dummy.next=head

        s=dummy
        f=head

        while f and f.next:
            s=s.next
            f=f.next.next
        
        s.next=s.next.next
        return head