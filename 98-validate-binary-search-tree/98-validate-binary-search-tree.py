# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        def inod(root):
            if root:
                inod(root.left)
                inorder.append(root.val)
                inod(root.right)
            
        inod(root)
        return all([a<b for a,b in zip(inorder,inorder[1:])])
                
    
        