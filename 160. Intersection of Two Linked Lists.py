# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr = headA
        a = 0
        while curr:
            a += 1
            curr = curr.next
        curr = headB
        b = 0
        while curr:
            b += 1
            curr = curr.next
        currA = headA
        currB = headB
        if a > b:
            for i in range(a - b):
                currA = currA.next 
        if a < b:
            for i in range(b - a):
                currB = currB.next
        if currA == currB:
            return currA            
        while currA.next:           
            if currA.next == currB.next:
                return currA.next
            currA = currA.next
            currB = currB.next
        
        return None
