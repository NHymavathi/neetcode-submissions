# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def add(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None

            total = carry

            if l1:
                total += l1.val

            if l2:
                total += l2.val

            node = ListNode(total % 10)

            node.next = add(
                l1.next if l1 else None,
                l2.next if l2 else None,
                total // 10
            )

            return node

        return add(l1, l2, 0)