'''
the problem is to find the time to traverse from one point to another

Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Runtime: 48 ms, faster than 99.02% of Python3 online submissions
Memory Usage: 14 MB, less than 97.88% of Python3 online submissions
'''
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for p in range(len(points)-1):
            point1 , point2 = points[p] , points[p+1]
            time += max(abs(point1[0] - point2[0]) , abs(point1[1] - point2[1]))
        return time
