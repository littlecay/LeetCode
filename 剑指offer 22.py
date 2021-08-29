# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        ptr = head
        print(head)
        li = []
        li.append(ptr)
        while ptr.next:
            ptr = ptr.next
            li.append(ptr)
            print(li)
        return li[-k]
