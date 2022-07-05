class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in nums:
            heapq.heappush(heap,-i)
        print(heap)    
        while k > 0:
            h = heapq.heappop(heap)
            k -= 1
        return -h
            
            
        
        