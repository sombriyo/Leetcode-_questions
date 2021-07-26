'''
The question is to find the highest altitude 
of the biker to travel

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Runtime: 36 ms, faster than 63.69% of Python3 online submissions
Memory Usage: 14.1 MB, less than 68.66% of Python3 online submissions
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        for i in range(len(gain)):
            altitude += gain[i]
            if altitude > highest:
                highest = altitude
        return highest 
            
            
