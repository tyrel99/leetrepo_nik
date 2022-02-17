class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #create res outside function
        res = []
        
        #create fun to add condition
        def dfs(i,curr,total):
            
            
            #if target == total / add curr to res / and return
            if total == target:
                res.append(curr.copy())
                return
            
            # if i exceed len of array /  or total > target / return
            if i >= len(candidates) or total > target:
                return
            
            #create recursive function
            curr.append(candidates[i])
            dfs(i,curr,total + candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
        
        dfs(0,[],0)
        return res
            
            
        
        