class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        count = Counter(num)
        print(count)
        s = ''.join(count[i] // 2 * i for i in "9876543210").lstrip("0")
        mid  = max(count[i] % 2 * i for i in count)
        return s + mid + s[::-1] or "0"
     