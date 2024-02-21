#268. Missing Number

#Given an array nums containing n distinct numbers in the range [0, n], 
#return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minm=min(nums)
        maxm=max(nums)
        nums1=[i for i in range(minm,maxm+1)]
        if 0 not in nums:
            return 0
        elif set(nums) == set(nums1):
            return maxm+1
        else:
            return sum(nums1)-sum(nums)
