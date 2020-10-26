# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(root, val):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = helper(root.right, val)
                return root
            else:
                root.left = helper(root.left, val) 
                return root
        
        root = TreeNode(preorder[0])
        for i in range(len(preorder)-1):
            helper(root, preorder[i+1])
        return root
