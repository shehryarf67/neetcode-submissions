# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        n = len(nodes)

        for i in range(0, n - k + 1, k):
            first = i
            last = i + k - 1

            while first < last:
                nodes[first], nodes[last] = nodes[last], nodes[first]
                first += 1
                last -= 1

        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]

        nodes[-1].next = None

        return nodes[0]