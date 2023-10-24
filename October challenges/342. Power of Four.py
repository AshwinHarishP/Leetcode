class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n != 0 or n < 0:
            return False
        return isPowerOfFour(n // 2)
        
