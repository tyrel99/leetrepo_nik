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
        res = []
        next_que = []
        while queue:
            temp = []
            for root in queue:
                temp.append(root.val)
                if root.left:
                    next_que.append(root.left)
                if root.right:
                    next_que.append(root.right)
            res.append(temp.pop())
            queue = next_que
            next_que = []
        return res
                    
                
        
        