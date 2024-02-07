#451. Sort Characters By Frequency

#Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
#Return the sorted string. If there are multiple answers, return any of them.

from collections import Counter,OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        r = OrderedDict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        ans = ''.join([c * f for c, f in r.items()])
        return ans
