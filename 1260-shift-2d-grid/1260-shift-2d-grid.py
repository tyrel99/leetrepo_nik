class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        Nr = len(grid)         #len(row)
        Nc = len(grid[0])      #len(col)
        
        li = [0] * Nr * Nc     #temp list
        
        k = k % (Nr * Nc)      #If k is greater than the length of vector, 
		                       # the shift will repeat itself in a cycle; 
		                       # hence, we only care about the remainder.  
        
        for i in range(Nr):
            for j in range(Nc):
                li[i * Nc + j] = grid[i][j]
        
        self.Rev(li, 0, Nr * Nc -1)  #Reverse whole grid
        self.Rev(li, 0, k-1)         #Reverse first k elements
        self.Rev(li, k, Nr * Nc - 1) #Reverse last k elements
        
        
                
        for i in range(Nr):
            for j in range(Nc):
                grid[i][j] = li[i * Nc + j]
                
        return grid
    
    def Rev(self,li,left,right):
        while left < right:
            li[left], li[right] = li[right], li[left]
            left += 1
            right -= 1
        