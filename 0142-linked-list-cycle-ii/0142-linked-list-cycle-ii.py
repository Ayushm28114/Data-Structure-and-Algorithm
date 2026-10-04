# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow==fast:
                fast=head

                while slow!=fast:
                    slow, fast = slow.next, fast.next
                return fast
        return