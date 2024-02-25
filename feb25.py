#2709. Greatest Common Divisor Traversal

#You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. 
#You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.
#Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.
#Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

class Solution:
    def dfs(self, index, visitedIndex, visitedPrime):
        if visitedIndex[index]:
            return
        visitedIndex[index] = True

        for prime in self.index2prime[index]:
            if visitedPrime.get(prime, False):
                continue
            visitedPrime[prime] = True
            for index1 in self.prime2index[prime]:
                if visitedIndex[index1]:
                    continue
                self.dfs(index1, visitedIndex, visitedPrime)

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        self.prime2index = {}
        self.index2prime = {}
        for i, num in enumerate(nums):
            temp = num
            for j in range(2, int(num ** 0.5) + 1):
                if temp % j == 0:
                    self.prime2index.setdefault(j, []).append(i)
                    self.index2prime.setdefault(i, []).append(j)
                    while temp % j == 0:
                        temp //= j
            if temp > 1:
                self.prime2index.setdefault(temp, []).append(i)
                self.index2prime.setdefault(i, []).append(temp)

        visitedIndex = [False] * len(nums)
        visitedPrime = {}
        self.dfs(0, visitedIndex, visitedPrime)

        return all(visitedIndex)
