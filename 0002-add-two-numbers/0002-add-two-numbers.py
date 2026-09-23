# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur, curr = l1, l2
        a, b = [], []

        while cur or curr:
            if cur:
                a.append(cur.val)
                cur = cur.next
            if curr:
                b.append(curr.val)
                curr = curr.next
        
        m="".join(map(str,a))
        n="".join(map(str,b))

        p=int(m[::-1])
        q=int(n[::-1])

        r=p+q

        dummy=ListNode(-1)
        cr=dummy
        
        if r==0:
            cr.val=0
            return cr

        while r>0:
            a=ListNode(r%10)
            cr.next=a
            cr=cr.next
            r//=10
        return dummy.next