'''
Given an array of positive integers nums and a positive
integer target, return the minimal length of a contiguous subarray
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than
or equal to target. If there is no such subarray, return 0 instead.
'''

def two_pointer(nums, s):
    p1 = 0
    p2 = 0

    total = 0
    res = float('inf')

    while (p2 < len(nums)):
        total +=  nums[p2]
        if total < s:
            p2 += 1
        else:
            # this line calculate the minimum length
            res = min(res, p2 - p1 + 1)
            total = total - nums[p1] - nums[p2]
            p1 += 1

    return res if res < float('inf') else 0

nums = [2,3,1,2,4,3]
target = 7
print(two_pointer(nums, target))