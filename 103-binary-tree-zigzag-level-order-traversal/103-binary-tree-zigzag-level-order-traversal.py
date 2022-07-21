# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        
        queue = deque([root])
        level = 0
        res = []
        
        while queue:
            d = deque()
            lenq = len(queue)
              
            for i in range(lenq):
                node = queue.popleft()
                
                if level % 2 != 0:
                    d.appendleft(node.val)
                else:
                    d.append(node.val)
                    
                if node.left : queue.append(node.left),
                if node.right : queue.append(node.right),
            res.append(d)
            level += 1
        return res
        
        