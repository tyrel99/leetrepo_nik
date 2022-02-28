# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            hl = dfs(root.left)
            hr = dfs(root.right)
            
            if abs(hl - hr) > 1:
                self.res = False
            return max(hl,hr) + 1
        self.res = True
        dfs(root)
        return self.res
        