class Solution:
    def reverseString(self, s: List[str]) -> None:
        #USING RECURSSION
        N = len(s)
        def swap(i):
            #base condition
            if i >= N//2:
                return
            s[i], s[N-i-1] = s[N-i-1], s[i]
            swap(i+1)
        swap(0)
        
        """
        Do not return anything, modify s in-place instead.
        """
        