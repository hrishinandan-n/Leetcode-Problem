class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        current = n
        while True: 
            temp = current
            pdt = 1
            
            while temp > 0:
                rem = temp % 10
                pdt *= rem
                temp = temp // 10
                
            if pdt % t == 0:
                return current
                    
            current = current + 1