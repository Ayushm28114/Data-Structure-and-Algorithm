# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
                
        dummy = ListNode(float('-inf'))
        i,j,k = dummy,head,head.next
        
        while k!=None:
            j.next=i
            i=j
            j=k
            k=k.next
        
        j.next=i

        curr=j
        while curr.next!=dummy:
            curr=curr.next
        curr.next=None
        return j