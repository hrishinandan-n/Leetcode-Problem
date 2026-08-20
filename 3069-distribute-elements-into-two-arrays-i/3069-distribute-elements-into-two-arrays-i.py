class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [], []
        x, y = nums[0], nums[1]
        arr1 += [x]
        arr2 += [y]
        for i in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1 += [i]
            else:
                arr2 += [i]
        
        result = arr1 + arr2
        return result
