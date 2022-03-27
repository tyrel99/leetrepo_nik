class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        hashh = {}
        
        for i in range(len(mat)):
            counts = mat[i].count(1)
            hashh[i] = counts
            counts = 0
            
        new_hash = sorted(hashh.items(),key = lambda x : x[1])
        print(new_hash)
        
        i = 0
        while i < k:
            res.append(new_hash[i][0])
            i+= 1
        
        return res
            
        
        
        