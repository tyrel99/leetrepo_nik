class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for i in nums:
            if not res or i != res[-1][-1] + 1:
                if res and len(res[-1]) >= 2:
                    res[-1] = [res[-1][0]] + [res[-1][-1]]
                res.append([i])
            else:
                res[-1].append(i)
        if res and len(res[-1]) >= 2:
            res[-1] = [res[-1][0]] + [res[-1][-1]]
                
        return ['->'.join(map(str,x)) for x in res]
        