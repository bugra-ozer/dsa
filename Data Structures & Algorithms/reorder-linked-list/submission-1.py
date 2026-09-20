# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second_half = self.reverseNode(slow.next)
        slow.next=None

        p1 = head
        p2 = second_half

        while p2:
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next

    def reverseNode(self, node):
        prev=None
        curr=node
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev

