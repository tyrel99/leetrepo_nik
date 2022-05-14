class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Create the dict to store the values
        edges = collections.defaultdict(list)
        
        for u,v,w in times:
            edges[u].append((v,w))
        
        #create the variables 
        min_heap = [(0,k)]   #insert the first value
        visit = set()
        time = 0
        
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)    
            time = max(time, w1)
                
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap,(w1 + w2, n2))
                    
        return time if len(visit) == n else -1
                    
                    
                    
        
        
        