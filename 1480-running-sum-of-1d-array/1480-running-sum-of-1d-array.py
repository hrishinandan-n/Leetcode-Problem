class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        arr = []

        for k, v in enumerate(nums):
            total += v
            arr += [total]

        return arr
