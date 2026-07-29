"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        copies = {}
        current = head

        # First pass: create a copy of every node
        while current:
            copies[current] = Node(current.val)
            current = current.next

        current = head

        # Second pass: connect next and random pointers
        while current:
            copied_node = copies[current]

            copied_node.next = copies.get(current.next)
            copied_node.random = copies.get(current.random)

            current = current.next

        return copies[head]