'''
we are given only 2 fruit basket we need to pick up
maximum fruits possible from the farm array.
each basket can hold any number of fruits
'''

def using_hashing(nums):
    store = [0]* len(nums)
    for i in nums:
        store[i] += 1
    #store.sort()
    max_fruits = store[-1] + store[-2]
    print(store)
    return max_fruits


fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(using_hashing(fruits))