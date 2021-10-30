'''
The questions is to find the number of squares of largest lenght that can be fromed
Runtime: 184 ms, faster than 73.32% of Python3 online submissions
Memory Usage: 14.6 MB, less than 98.98% of Python3 online submissions 
'''

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        some = []
        for i in rectangles:
            some.append(min(i))
        return some.count(max(some))
        
