# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while self.isNodesValid(slow, fast):
            if fast is slow:
                return True
            fast=fast.next.next
            slow=slow.next
        return False
        
    def isNodesValid(self, slow, fast):
        if slow is not None and fast is not None and fast.next.next is not None:
            return True
        return False