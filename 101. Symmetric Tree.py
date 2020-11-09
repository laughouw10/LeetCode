# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        root1 = root.left
        root2 = root.right
        stack1 = []
        stack2 = []
        
        while True:
            if root1 == None and root2 == None:
                if not stack1 and not stack2:
                    return True
                elif stack1 and stack2:
                    root1 = stack1.pop().right
                    root2 = stack2.pop().left
                else:
                    return False
             
            elif root1 and root2 and root1.val == root2.val:
                stack1.append(root1)
                stack2.append(root2)
                root1 = root1.left
                root2 = root2.right
                
            else:
                return False

        return True
