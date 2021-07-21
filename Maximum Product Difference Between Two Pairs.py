'''
Find the maximum difference of the product
Runtime: 156 ms, faster than 97.41% of Python3
Memory : 15.4 MB, less than 53.06% of Python3 
TC: O(nlogn)
SC : O(n)
'''
  def maxProductDifference(self, nums: List[int]) -> int:
      nums.sort()
      diff = nums[len(nums)-1] * nums[len(nums)-2] - nums[0]*nums[1]
      return diff
