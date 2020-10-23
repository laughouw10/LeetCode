# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        curr = head
        n = 0
        lst = []
        while curr:
            n += 1
            lst.append(curr.val)
            curr= curr.next
        
        def build_tree(lst, n):
            if not lst:
                return
            
            if n == 1:
                if len(lst) == 1:
                    return TreeNode(lst[0])
                else:
                    return
            
            mid = n //2
            rootnode = TreeNode(lst[n//2])
            left_lst = lst[:mid]
            right_lst = lst[mid+1:]
            
            rootnode.left = build_tree(left_lst, mid)
            rootnode.right = build_tree(right_lst, len(lst) - mid - 1)
            return rootnode
        return build_tree(lst, n)
