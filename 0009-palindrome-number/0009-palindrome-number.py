class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        if number < 0:
            return False
        remainder = 0
        reverse = 0
        while x != 0:
            remainder = x % 10
            reverse = remainder + (reverse * 10)
            x //= 10
        
        if reverse == number:
            return True
        return False