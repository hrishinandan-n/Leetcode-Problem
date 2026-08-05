class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        def find_number(arr):
            number = 0
            for i in arr:
                number *= 10
                number += i

            return number

        def convert_number(num):
            if num == 0:
                return [0]
                
            arr = []
            rem = 0
            while num > 0:
                rem = num % 10
                arr += [rem]
                num //= 10
            
            return arr

        def reverse_arr(arr):
            length = 0
            for i in arr:
                length += 1
            
            for i in range(length//2):
                j = length - i - 1
                arr[i], arr[j] = arr[j], arr[i]
            
            return arr
        number = find_number(digits)
        number += 1
        arr = convert_number(number)
        arr = reverse_arr(arr)
        
        return arr
