# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minn = min(p.val,q.val)
        maxx = max(p.val,q.val)
        
        while root:
            if maxx < root.val:
                root = root.left
            elif minn > root.val:
                root = root.right
            else:
                return root
        