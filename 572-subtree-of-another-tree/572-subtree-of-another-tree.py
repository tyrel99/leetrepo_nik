# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False
        
        sameTree = self.isSametree(root,subRoot)
        subleft = self.isSubtree(root.left,subRoot)
        subright = self.isSubtree(root.right,subRoot)
        
        return subleft or subright or sameTree
        
        
        
    def isSametree(self,root,subRoot):
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val != subRoot.val:
            return False
        return self.isSametree(root.left,subRoot.left) and self.isSametree(root.right,subRoot.right)
        
        
        
        
        
        
        
        
        
        """  
        p = root
        q = subroot
        queue = [(p,q)]
        
        while queue:
            node1,node2 = queue.pop(0)
            if None in (node1,node2):
                return False
            if not node1 and not node2:
                continue
            else:
                if node1.val != node2.val:
                    queue.append((node1.left,node2))
                    queue.append((node2.right,node2))
        """
                
                    
        
        