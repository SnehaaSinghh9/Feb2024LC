#2108. Find First Palindromic String in the Array

#Given an array of strings words, return the first palindromic string in the array. 
#If there is no such string, return an empty string "".
#A string is palindromic if it reads the same forward and backward.

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans=[]
        for w in words:
            if (w==w[::-1]):
                ans.append(w)
            if ans!=[]:
                break
        if ans:
            return ans[0]
        else:
            return ""
