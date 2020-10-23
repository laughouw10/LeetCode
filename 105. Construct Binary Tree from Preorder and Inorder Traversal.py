# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        map = {}
        for i in range(len(inorder)):
            map[inorder[i]] = i
        def helper(P, startP, endP, I, startI, endI):
            if startP > endP:
                return
            rootnode = TreeNode(P[startP])
            rootindex = map[P[startP]]
            numleft = rootindex - startI
            rootnode.left = helper(P, startP + 1, startP + numleft, I, startI, rootindex - 1)
            rootnode.right = helper(P, startP + numleft + 1, endP, I, rootindex + 1, endI)
            return rootnode
        return helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
