'''
Need to find a triplet in an array whose sum is
equal to zero

nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''


def three_sum(nums):
    #sorting array to avoide duplicates
    nums.sort()
    #for storing output
    res = []

    for i in range(len(nums)):
        #checking if the consicutive numeber are same or not
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        #initializing the left and right pointer at the one place
        # ahead of i pointer and at the end of array respectively
        left = i + 1
        right = len(nums) - 1
        x = nums[i]
        while left < right:
            #if the sum if equal to zero
            if x + nums[left] + nums[right] == 0:
                res.append([x, nums[left], nums[right]])
                #if left pointer encounter consecutive duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # if right pointer encounter consecutive duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                #we are not going to stop even if the we found a triplet
                left += 1
                right -= 1
            # if the sum is less than zero increase left pointer
            elif x + nums[left] + nums[right] < 0:
                left += 1
            # if the sum is greater than zero decrease right pointer
            else:
                right -= 1
    #returing the output
    return res

nums = [-1,0,1,2,-1,-4]
print(three_sum((nums)))





