class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        dictt = defaultdict(int)
        
        for char in s:
            dictt[char] += 1
        
        for char in t:
            if dictt[char]:
                dictt[char] -= 1
            else:
                count += 1
        return sum(dictt.values())
        