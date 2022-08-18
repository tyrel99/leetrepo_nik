# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [[root,1]]
        res = 1
        while stack:
            node,idx = stack.pop()
            
            
            if node:
                res = max(res,idx)
                stack.append([node.left,idx+1])
                stack.append([node.right,idx+1])
        return res
            