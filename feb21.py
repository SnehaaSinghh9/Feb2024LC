#201. Bitwise AND of Numbers Range

#Given two integers left and right that represent the range [left, right], 
#return the bitwise AND of all numbers in this range, inclusive.

 class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res= 0
        while left != right:
            left >>= 1
            right >>= 1
            res += 1
        return left << res
