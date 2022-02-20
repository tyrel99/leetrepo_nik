class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        
        i = 0 
        while i < len(intervals)-1:
            a,b = intervals[i] 
            c,d = intervals[i+1]
            
            if a <= c and d <= b:
                intervals.remove(intervals[i+1])
                i -= 1
            
            elif a >= c and d >= b:
                intervals.remove(intervals[i])
                i -= 1
                
            i += 1
            
        return len(intervals)
        