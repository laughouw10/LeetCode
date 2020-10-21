# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = 0
        result = []
        current = head
        while current:
            n += 1
            current = current.next
        if n == 1:
            return True
        current = head
        for i in range(n//2):
            result.append(current.val)
            current = current.next
        while current:
            if current.val == result[-1]:
                result.pop()
            current = current.next
        return result == []
