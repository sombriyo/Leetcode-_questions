'''
well i didnt under stande the questions but here is the answer
Runtime : 208 ms, faster than 94.86% of Python3
Memory : 15 MB, less than 84.00% of Python3 
'''
class OrderedStream:
    def __init__(self, n):
        self.stream = [None]*n
        self.ptr = 0

    def insert(self, idKey, value):
        idKey -= 1
        self.stream[idKey] = value
        if self.ptr < idKey:
            return []
        else:
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                self.ptr += 1
            return self.stream[idKey:self.ptr]
