# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        level = []
        s1 = [root]
        s2 = []
        res = []
        while s1 or s2:
            while s1:
                node = s1.pop()
                level.append(node.val)
                if node.left is not None:
                    s2.append(node.left)
                if node.right is not None:
                    s2.append(node.right)
                
            res.append(level)
            level = []
            
            while s2:
                node = s2.pop()
                level.append(node.val)
                if node.right is not None:
                    s1.append(node.right)
                if node.left is not None:
                    s1.append(node.left)
            
            if level != []:
                res.append(level)
                level = []
        return res
            
    
            
            
            
        