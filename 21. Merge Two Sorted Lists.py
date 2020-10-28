# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        if not l1:
            return l2
        if not l2:
            return l1
        
        if head1.val <= head2.val:
            ans = ListNode(head1.val)
            head1 = head1.next
        else:
            ans = ListNode(head2.val)
            head2 = head2.next
        curr = ans
        while True:
            if head1 and head2:
                if head1.val == head2.val:
                    curr.next = ListNode(head1.val)
                    curr = curr.next
                    head1 = head1.next
                    
                elif head1.val > head2.val:
                    curr.next = ListNode(head2.val)
                    head2 = head2.next
                    curr = curr.next
                else:
                    curr.next = ListNode(head1.val)
                    head1 = head1.next
                    curr = curr.next
            else:
                break
        if head1:
            curr.next = head1
        else:
            curr.next = head2
        return ans21. Merge Two Sorted Lists
