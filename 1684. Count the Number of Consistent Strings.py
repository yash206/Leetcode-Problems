''' 
Question -
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
'''

'''
Difficulty - Easy
'''


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            stat = True
            for j in i:
                if j not in allowed:
                    stat = False
                    break
            if stat == False:
                continue
            count += 1
        return count



'''
Time Complexity - O(n*m)
'''
