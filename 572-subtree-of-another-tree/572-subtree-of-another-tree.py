# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) or self.sameTree(root,subRoot)
        
        
        
    def sameTree(self,root,subRoot):
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        
        return root.val == subRoot.val and self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right)
        