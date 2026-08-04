class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        def find_length(arr):
            length = 0
            for i in arr:
                length += 1
            return length

        def sorting(arr, length):
            for i in range(length-1):
                for j in range(i+1, length):
                    if arr[i]> arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]
            return arr

        def find_missing(arr):
            missing = []
            full_arr = [_ for _ in range(arr[0], arr[-1])]
            for i in full_arr:
                if i not in arr:
                    missing += [i]
            return missing

        length = find_length(nums)
        nums = sorting(nums, length)
        missing = find_missing(nums)
        
        return missing
