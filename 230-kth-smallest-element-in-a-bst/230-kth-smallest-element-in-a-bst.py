# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # WILL PERFORM BFS TRAVERSAL 
        arr = []
        
        queue = deque([root])
        
        while queue:
            lenq = len(queue)
            for i in range(lenq):
                node = queue.popleft()
                
                if node:
                    arr.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    
        arr.sort()
        return arr[k-1]
            
       