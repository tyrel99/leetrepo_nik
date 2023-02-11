class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        
        
        for i,j in redEdges:
            red[i].append(j)
            
        for i,j in blueEdges:
            blue[i].append(j)
       
        ans = [-1 for _ in range(n)]
        
        queue = deque()
        queue.append([0, 0, None])
        
        visit = set()
        visit.add((0,None))
        
        while queue:
            node, dist, prevC = queue.popleft()
            
            if ans[node] == -1:
                ans[node] = dist
            
            if prevC != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        queue.append([nei, dist+1, "RED"])
                        
            if prevC != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        queue.append([nei, dist+1, "BLUE"])
                        
        return ans
            
            