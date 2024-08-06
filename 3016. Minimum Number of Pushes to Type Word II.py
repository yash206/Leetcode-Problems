'''
Question - 
You are given a string word containing lowercase English letters.
Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .
It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.
Return the minimum number of pushes needed to type word after remapping the keys.
'''

'''
Difficulty - Medium
'''


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for i in word:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        ans = 0
        pushes = 1
        n = 0
        for key, value in freq:
            if n==8:
                n=0
                pushes += 1
            ans = ans + value*pushes
            n+=1
        return ans


'''
Time Complexity - O(nlogn)
'''
