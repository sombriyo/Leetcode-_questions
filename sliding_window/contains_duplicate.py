'''
Tip : if you ever encounter duplicates use of hashmap
is better choice
'''
#--------------------------------------------------------------------------
'''
Given an integer array nums and an integer k, return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

def contains_duplicate_bf(nums, k):
    # this one talking too much time
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums [j]:
                print(i,j)
                if abs(i-j) <= k:
                    return True
    return False


def efficient_apporach(nums, k):
    '''
    O(n) time and space
    but faster than BF
    Runtime: 584 ms, faster than 93.33% of Python3 online submissions
    Memory Usage: 28.4 MB, less than 43.65% of Python3 online submissions
    '''
    #Storing the number in the dict
    # like number:index
    lookup = {}
    for i, num in enumerate(nums):
        if num not in lookup:
            lookup[num] = i
        else:
            #condition 2 substract the current index with
            # the index of previously found same element
            if i - lookup[num] <= k:
                return True
            #updating the index of a numeber
            lookup[num] = i
    return False



nums = [1,2,3,1,2,3]
k = 3
print(efficient_apporach(nums, k))