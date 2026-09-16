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
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                return True
        return False
        
    def isNodesValid(self, slow, fast):
        if slow is not None and fast is not None:
            try: 
                if fast.next.next is not None:return True
            except AttributeError:
                return False
        return False