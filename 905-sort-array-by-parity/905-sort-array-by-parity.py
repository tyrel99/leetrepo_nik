class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lis = []
        for i in nums:
            if i % 2 == 0:
                lis.append(i)
        for i in nums:
            if i % 2 == 1:
                lis.append(i)
        return lis
        