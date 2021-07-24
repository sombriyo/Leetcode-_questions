'''
You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
-------------------------------------------------------------------------
The logic is calulate the words that are not consistent and then substract it from all the 
words given

Runtime:216 ms, faster than 94.49% of Python3 online submissions 
Momory: 16.3 MB, less than 26.65% of Python3 online submissions
'''
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            for j in i:
                if(j not in allowed):
                    c+=1
                    break
        return len(words)-c
