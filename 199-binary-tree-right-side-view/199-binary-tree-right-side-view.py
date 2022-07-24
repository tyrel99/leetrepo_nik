# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            rtval = None
            lenq = len(queue)
            
            for i in range(lenq):
                node = queue.popleft()
               
                
                if node : 
                    rtval = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rtval:   
                res.append(rtval.val)
           
        return res
        