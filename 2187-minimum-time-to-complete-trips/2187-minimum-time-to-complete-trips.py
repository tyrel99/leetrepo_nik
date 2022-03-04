class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low, high = 1, 10 ** 14
        
        while low < high:
            mid = low + (high - low) // 2
            
            trips = sum(mid // t for t in time)
            
            if trips < totalTrips:
                low = mid + 1
            else:
                high = mid
        return low
        