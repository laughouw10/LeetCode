# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        currA = head
        currB = head
        for i in range(n):
            currB = currB.next
        if not currB:
            head = head.next
        else:
            while currB.next:
                currA = currA.next
                currB = currB.next
            currA.next = currA.next.next
        return head
