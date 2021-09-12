''''
Given two integer arrays nums1 and nums2,
return the maximum length of a subarray that appears in both arrays.
'''



def using_strings(num1, num2):
    ''''
    The logic here is to convert the number into string and then
    match the strings
    1. convert one of the array into string say num1
    2. maintain the longest substring
    3. if the substring did not match remove the 1st element of the maxstring
    
    Runtime: 167 ms, faster than 96.95% of Python3 online submissions
    Memory Usage: 14.4 MB, less than 92.09% of Python3 online submissions
    '''
    num2_str = ''.join([chr(x) for x in num2])
    count = 0
    max_str = ''
    for i in num1:
        max_str += chr(i)
        if max_str in num2_str:
            count = max(count, len(max_str))
        else:
            max_str = max_str[1:]
    return count



nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]

print(using_strings(nums1, nums2))