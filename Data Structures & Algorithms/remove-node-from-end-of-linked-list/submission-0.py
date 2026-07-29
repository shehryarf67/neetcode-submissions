# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        current = head
        while current:
            nodes.append(current)
            current = current.next

        i = len(nodes) - n

        # Removing the head
        if i == 0:
            return head.next

        # Removing the tail
        if i == len(nodes) - 1:
            nodes[i - 1].next = None
        else:
            # Removing a middle node
            nodes[i - 1].next = nodes[i + 1]

        return head