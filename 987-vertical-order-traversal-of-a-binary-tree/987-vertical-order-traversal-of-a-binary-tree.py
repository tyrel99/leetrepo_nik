# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root,0)])
        hashh = defaultdict(list)
        
        while queue:
            temp = []
            d = defaultdict(list)
            
            for node,idx in queue:
                d[idx].append(node.val)
                if node.left : temp += (node.left,idx-1),
                if node.right : temp += (node.right,idx+1),
                    
            for i in d : hashh[i].extend(sorted(d[i]))
            
            queue = temp
        return [hashh[i] for i in sorted(hashh)]
                