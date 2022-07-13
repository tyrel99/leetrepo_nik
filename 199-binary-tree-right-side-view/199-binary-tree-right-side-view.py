# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        level = []
        res = []
        
        while queue != []:
            for node in queue:
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)
            res.append(node.val)
            
            queue = level
            level = []
        
        
            
            
        return res
        
        