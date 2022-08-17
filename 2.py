# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tree = ListNode(0)
        head = tree
        tmp = 0
        cur = 0
        while tmp or l1 or l2:
            cur = tmp
            if l1:
                cur = l1.val + cur
                l1 = l1.next
            if l2:
                cur = l2.val + cur
                l2 = l2.next
            tmp = cur // 10
            cur = cur % 10
            tree.next = ListNode(cur)
            tree = tree.next
        return head.next
