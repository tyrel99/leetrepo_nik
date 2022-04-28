# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        
        while root or stack:
            
            while root:
                stack.append(root)   # rootnode append
                root = root.left
                
            root = stack.pop()       # pop recent ele
            k -= 1
            if k == 0:             
                return root.val
            
            root = root.right        # right root appended
        