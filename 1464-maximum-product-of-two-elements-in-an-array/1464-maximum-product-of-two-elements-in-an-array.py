class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def find_length(arr):
            length = 0
            for i in arr:
                length += 1
            return length


        def sorting(arr):
            arr_length = find_length(arr)
            for i in range(arr_length -1):
                for j in range(i+1, arr_length):
                    if arr[i] <= arr[j]:
                        temp = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
            
            return arr
        
        nums = sorting(nums)
        larger, largest = nums[0], nums[1]
        product = (larger - 1)*(largest - 1)

        return product
