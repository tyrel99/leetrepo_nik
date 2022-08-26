# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        level = []
        next_que = []
        res = []
        
        while queue != []:
            for root in queue:
                level.append(root.val)
                
                if root.left:
                    next_que.append(root.left)
                if root.right:
                    next_que.append(root.right)
            
            res.append(level)
            level = []
            queue = next_que
            next_que = []
        return res
                
            
                    
        
        
        