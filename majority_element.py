class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Runtime: 164 ms, faster than 76.44% of Python3
        Memory Usage: 15.6 MB, less than 11.60% of Python3
        '''
        table = {}
        s = set(nums)
        for i in s:
            table[nums.count(i)] = i
        max_value = max(table.keys())
        return table[max_value]
