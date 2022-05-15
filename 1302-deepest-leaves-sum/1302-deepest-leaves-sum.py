# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        pre_level = []
        trav_queue = [root]
        
        while trav_queue:
            next_level = []
            
            for root in trav_queue:
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
                    
            pre_level, trav_queue = trav_queue, next_level
            
        return sum(node.val for node in pre_level if node)
                
                
        