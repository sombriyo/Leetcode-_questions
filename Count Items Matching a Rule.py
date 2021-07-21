'''
Question is to count matching pairs from the given 
2D array
Runtime : 236 ms, faster than 89.77% of Python3
Memory : 20.7 MB, less than 23.50% of Python3
TC -  O(n) SC - O(1)
'''
 def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in items:
            if ruleKey == "color" and ruleValue == i[1]:
                    count += 1
            elif ruleKey == "type" and ruleValue == i[0]:
                    count += 1
            elif ruleKey == "name" and ruleValue == i[2]:
                    count += 1
        return count

