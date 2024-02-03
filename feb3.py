#1043. Partition Array for Maximum Sum

#Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. 
#After partitioning, each subarray has their values changed to become the maximum value of that subarray.
#Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        def dfs(i):
            if i == n:
                return 0
            curMax = curSum = 0
            for j in range(i, min(i + k, n)):
                curMax = max(curMax, arr[j])
                cur = curMax * (j - i + 1) + dfs(j + 1)
                curSum = max(curSum, cur)
            return curSum
            
        return dfs(0)
