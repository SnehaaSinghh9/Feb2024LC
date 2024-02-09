#368. Largest Divisible Subset

#Given a set of distinct positive integers nums, return the largest subset answer 
#such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
#answer[i] % answer[j] == 0, or
#answer[j] % answer[i] == 0
#If there are multiple solutions, return any of them.

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        groupSize = [1] * n
        prevElement = [-1] * n
        maxIndex = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if groupSize[i] < 1 + groupSize[j]:
                        groupSize[i] = 1 + groupSize[j]
                        prevElement[i] = j
            if groupSize[i] > groupSize[maxIndex]:
                maxIndex = i
        ans = []
        while maxIndex != -1:
            ans.insert(0, nums[maxIndex])
            maxIndex = prevElement[maxIndex]
        return ans
