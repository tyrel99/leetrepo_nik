# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])
        res = []
        
        while queue:
            right_asu = None
            qlen = len(queue)
            
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    right_asu = node
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if right_asu:
                res.append(right_asu.val)
        return res
        
        