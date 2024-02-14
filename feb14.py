#2149. Rearrange Array Elements by Sign

#You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
#You should rearrange the elements of nums such that the modified array follows the given conditions:
#Every consecutive pair of integers have opposite signs.
#For all integers with the same sign, the order in which they were present in nums is preserved.
#The rearranged array begins with a positive integer.
#Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n_neg=[i for i in nums if i<0]
        n_pos=[i for i in nums if i>0]

        res=[]
        for i,j in zip(n_pos,n_neg):
            res.append(i)
            res.append(j)
        return res
