#1481. Least Number of Unique Integers after K Removals

#Given an array of integers arr and an integer k. 
#Find the least number of unique integers after removing exactly k elements.

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        a = sorted(Counter(arr).values())
        for i, j in enumerate(a):
            k = k-j
            if k < 0:
                return len(a) - i
        return 0
