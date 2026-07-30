# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        place = 1

        while l1 or l2:
            if l1:
                num1 += l1.val * place
                l1 = l1.next

            if l2:
                num2 += l2.val * place
                l2 = l2.next

            place *= 10

        result = num1 + num2

        dummy = ListNode()
        curr = dummy

        if result == 0:
            return ListNode(0)

        while result > 0:
            digit = result % 10
            curr.next = ListNode(digit)
            curr = curr.next
            result //= 10

        return dummy.next