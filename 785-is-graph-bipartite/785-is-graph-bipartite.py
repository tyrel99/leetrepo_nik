class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colored = {}
        
        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 1
                q = collections.deque([i])
                while q:
                    curr = q.popleft()
                    for nb in graph[curr]:
                        if nb not in colored:
                            colored[nb] = -colored[curr]
                            q.append(nb)
                        elif colored[nb] == colored[curr]:
                            return False
        return True
        