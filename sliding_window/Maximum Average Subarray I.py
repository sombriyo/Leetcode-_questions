'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
'''

def max_something(nums, k):
    '''
    here k is window length
    complexities :
    tc= O(n)
    sc = O(1)
    TLE - time limit exceeded
    '''
    p1 = 0

    max_avg = 0
    while True:
        p2 = p1 + k
        some = sum(nums[p1:p2]) / k
        if max_avg < some:
             max_avg = some
        if p2 == len(nums) - 1:
            break
        p1 += 1
    return float("{0:.5f}".format(max_avg))

def more_efficient(nums, k):
    ''''
    Sliding window technique
    in which you will calculate the sum of
    the window and as you move window right you'll substract
    the first element from the left in the sum
    Runtime: 1128 ms, faster than 98.53% of Python3 online submissions
    Memory Usage: 25.8 MB, less than 67.43% of Python3 online submissions
    '''
    best = now = sum(nums[:k])
    for i in range(k, len(nums)):
        now += nums[i] - nums[i - k]
        if now > best:
            best = now
    return best / k


nums = [1,12,-5,-6,50,3]
k = 4
print(more_efficient(nums, k))