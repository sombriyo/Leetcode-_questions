'''
The problem is to find the odd digits in the matrix 
after applying the operations

Runtime: 40 ms, faster than 88.31% of Python3 online submissions
Memory Usage: 14.5 MB, less than 22.79% of Python3 online submissions
    


Algorithm:
1. We count how many indices on each row and column
2. If count in a row or column is even, it doesn't matter
  If count in a row or column is odd, its effect as it has one indices
3. Now we wonder how many row and column have odd indices.
  We reduce the answer to variable cnt.
  cnt[0] contain count of odd indices of row
  cnt[1] contain count of odd indices of column
4. Result is row influence + column influence - overlapping*2
  Row influence = cnt[0]*m where m is length of column
  Column influence = cnt[1]*n where n is length of row
  Overlap = cnt[0]*cnt[1]. Since it had been count twice, we need to subtract it twice
'''
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # Extract odd occurance in row and col
        cnt = [sum(val%2 for val in Counter(idxs).values()) for idxs in zip(*indices)]
        return m*cnt[0] + n*cnt[1] - 2*cnt[0]*cnt[1]
