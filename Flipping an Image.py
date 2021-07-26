'''
Flipping and image

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Runtime: 44 ms, faster than 95.29% of Python3 online submissions 
Memory Usage: 14.4 MB, less than 25.54% of Python3 online submissions
'''

class Solution:
  def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
      x = len(image)
      y = len(image[0])
      for i in range(x):
          image[i] = image[i][::-1]
          for j in range(y):
              image[i][j] = abs(image[i][j] - 1)
      return image

