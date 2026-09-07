# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        b=head

        while b:
            a.append(b.val)
            b=b.next
        
        b=head
        a=a[::-1]
        
        for num in a:
            if num!=b.val:
                return False
            b=b.next
        return True