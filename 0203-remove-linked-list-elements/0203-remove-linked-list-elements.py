# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        a=dummy
        b=dummy.next

        while b:
            if b.val!=val:
                b=b.next
                a=a.next
            else:
                a.next=b.next
                b=b.next
        
        return dummy.next