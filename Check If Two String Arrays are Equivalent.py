'''
Join two Strings  which are given in the form of list
Runtime: 24 ms, faster than 96.62% of Python3 online submissions 
Memory: 13.9 MB, less than 99.53% of Python3 online submissions
'''

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
