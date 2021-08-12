'''
the questions is to find the sum of 
primary and secondary diagonal elements
Runtime: 108 ms, faster than 56.90% of Python3 
Memory Usage: 14.5 MB, less than 49.43% of Python3
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = 0
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            output += mat[i][i] 
            if cols-i-1 != i:
                output += mat[i][cols-i-1]
        return output

        
