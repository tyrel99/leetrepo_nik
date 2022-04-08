class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i,n in enumerate(nums):
            summ = target - n
            if summ in dictt:
                return [dictt[summ],i]
            dictt[n] = i
        return
        