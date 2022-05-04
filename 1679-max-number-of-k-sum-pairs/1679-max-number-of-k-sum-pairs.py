class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c,ans = Counter(nums), 0
        
        for val in c:
            ans += min(c[val],c[k-val])
        return ans//2
        
            
        