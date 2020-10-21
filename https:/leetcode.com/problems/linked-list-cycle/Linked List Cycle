# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        sp = head
        fp = head.next
        while sp != fp:
            if not fp or not fp.next:
                return False
            sp = sp.next
            fp = fp.next.next
        return True
