#231. Power of Two

#Given an integer n, return true if it is a power of two. Otherwise, return false.
#An integer n is a power of two, if there exists an integer x such that n == 2x.

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 0):
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
                
        return True
        
