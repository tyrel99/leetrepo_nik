class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != "*" and count == 0:
                res += s[i]
            elif s[i] != "*" and count != 0:
                count -= 1
            else:
                count += 1
        return "".join(res[::-1])
            