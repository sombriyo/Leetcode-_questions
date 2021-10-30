'''
the logic is to add the string to an empty list if it does not exist already
then return the len of the list

Runtime: 28 ms, faster than 96.24% of Python3 online submissions
Memory Usage: 14.4 MB, less than 5.51% of Python3 online submissions
'''
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        x=[]
        for j in words:
            w=j
            s=""
            for i in w:
                s+=d[ord(i)-97]
            if(s not in x):
                x.append(s)
                
        return len(x)
                
                
