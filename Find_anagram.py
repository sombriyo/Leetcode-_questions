'''
Simple code to find anagrams
TC: O(n)
SC: O(n)
'''


def find_anagrams(A, B):
    lookup = {val:index for index, val in enumerate(B)}
    return [lookup[i] for i in A]
