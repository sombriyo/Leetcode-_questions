'''
Runtime : 1448 ms, faster than 8.38% of Python3 online submissions
Memory Usage: 14.2 MB, less than 86.63% of Python3 online submissions 

ik this looks like a shitty code buy that all i can do right now 
'''






class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if i < j and j < k:
                        if abs(arr[i] - arr[j]) <= a:
                            if abs(arr[j] - arr[k]) <= b:
                                if abs(arr[i] - arr[k]) <= c:
                                    count += 1
        return count
        
