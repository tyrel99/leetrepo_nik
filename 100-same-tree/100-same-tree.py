# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        
        while stack:
            cp,cq = stack.pop()
            if not cp and not cq:
                continue
            elif None in (cp,cq):
                return False
            
            else:
                if cp.val != cq.val:
                    return False
                stack.append((cp.left,cq.left))
                stack.append((cp.right,cq.right))
        return True
            
        
        