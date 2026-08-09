class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        arr = []

        for i in nums:
            total += i
            arr += [total]
        
        return arr