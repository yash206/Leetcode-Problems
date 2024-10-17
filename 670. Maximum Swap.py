''' 
Question -
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.
'''

'''
Difficulty - Medium
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert num to a list of characters
        s = list(str(num))
        
        # Store the last occurrence positions of digits 0-9
        lpos = [-1] * 10
        for i in range(len(s) - 1, -1, -1):
            val = int(s[i])
            if lpos[val] == -1:
                lpos[val] = i

        # Check for possible swaps
        for i in range(len(s)):
            for j in range(9, int(s[i]), -1):
                # Swap with the largest digit that appears later
                if lpos[j] > i:
                    s[i], s[lpos[j]] = s[lpos[j]], s[i]
                    return int(''.join(s))

        return num


'''
Time Complexity - O(n)
'''
