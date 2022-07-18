class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        self.rows, self.cols = len(grid), len(grid[0])
        self.visit = set()
        islands = 0
        
        
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == '1' and (r,c) not in self.visit:
                    self.bfs(grid,r,c)
                    islands += 1
        return islands
    
    def bfs(self,grid,r,c):
            queue = collections.deque()
            self.visit.add((r,c))
            queue.append((r,c))
        
            while queue:
                row,col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(self.rows) and
                        c in range(self.cols) and 
                        grid[r][c] == '1' and 
                        (r,c) not in self.visit):
                    
                        queue.append((r,c))
                        self.visit.add((r,c))
    
    
    
                
            
        
        
        