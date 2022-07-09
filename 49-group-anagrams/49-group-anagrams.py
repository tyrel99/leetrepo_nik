class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashh = {}
        res = []
        
        
        for s in strs:
            sot = "".join(sorted(s))
            
            
            if sot not in hashh:
                hashh[sot] = [s]
            else:
                hashh[sot].append(s)
                
        for val in hashh.values():
            res.append(val)
            
        return res
    
                              
                
                
        
        
        