class Solution:
    def countEven(self, num: int) -> int:
        n, dsum = num, 0
        while n > 0:
            dsum += n % 10
            n = n // 10
        
        if num % 2 == 0 and dsum % 2 == 1:
            return num // 2 - 1
        return num // 2
                
        
        