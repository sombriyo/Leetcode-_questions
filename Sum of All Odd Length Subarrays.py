'''
TO find the sum of all subarrays which have odd length
for example:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

The solution has the following logic
1. count the coefficients for each of the numbers in the array
here coefficients means the number of times a particular number i.e arr[i]
appears while calculating sum.
2. then multiply the coefficient with the number and sum it all
3. we got the desired answer.
Formula to calculate coefficients 
((i + 1) * (len(arr) - i) + 1) // 2
where i is the index.

Runtime: 36 ms, faster than 94.67% of Python3 online submissions
Memory: 14.2 MB, less than 78.35% of Python3 online submissions
'''
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        Sum=0
        for i in range(len(arr)):
            Sum += ((((i + 1) *
                  (len(arr) - i) +
                 1) // 2) * arr[i])
        return Sum
        
