'''
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".

Runtime: 32 ms, faster than 59.94% of Python3 online submissions
Memory : 14.3 MB, less than 19.77% of Python3 online submissions
'''

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ''.join([s.split(' ')[i] + ' ' for i in range(k)])[:-1]
