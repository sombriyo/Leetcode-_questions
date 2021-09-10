''''
Given an array of integers nums and an integer k, return the number of
contiguous subarrays where the product of all the elements
in the subarray is strictly less than k.
'''

def efficient_apporach(nums, k):
    '''
    We initialised two pointers at 0 index
    we the right pointer to traverse the array and
    and simultaneously multiplying the elements
    and checking if the product is greater than the k value
    if yes we'll move the left pointer towards the right pointer
    and dividing the product by the left pointer elements before incrementing the
    left pointer
    Here the catch is we we'll store the subarray count
    in "right -left + 1" which will count all the sub array present

    Runtime: 724 ms, faster than 52.40% of Python3 online submissions
    Memory Usage: 16.8 MB, less than 64.57% of Python3 online submissions
    '''
    left = count = 0
    product = 1
    #right pointer
    for right in range(len(nums)):
        #doing product
        product *= nums[right]
        #checking the condition for left pointer movement
        if product >= k:
            while product >= k and left <= right:
                #dividing the product by left pointer elements
                product /= nums[left]
                left += 1
        # this is the catch of calculation sub arrays
        count += right - left + 1
    return count


nums = [1,2,4,8,10]
k = 20
print(efficient_apporach(nums,k))


