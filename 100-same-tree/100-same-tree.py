# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Bfs Traversal
        queue = [(p,q)]
        
        while queue:
            nd1,nd2 = queue.pop(0)
            
            if not nd1 and not nd2:
                continue
            elif None in (nd1,nd2):
                return False
            else:
                if nd1.val != nd2.val:
                    return False
                queue.append((nd1.left,nd2.left))
                queue.append((nd1.right,nd2.right))
                
        return True
        
        