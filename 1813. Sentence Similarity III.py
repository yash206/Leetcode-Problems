''' 
Question -
You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.
Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.
For example,
s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.
'''

'''
Difficulty - Medium
'''


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split both sentences into words
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Ensure sentence1 is the shorter one, swap if necessary
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        
        # Try to match the words from the start
        i = 0
        while i < len(words1) and words1[i] == words2[i]:
            i += 1
        
        # Try to match the words from the end
        j = 0
        while j < len(words1) and words1[-(j+1)] == words2[-(j+1)]:
            j += 1
        
        # If the matched prefix and suffix together cover all of words1, return true
        return i + j >= len(words1)


'''
Time Complexity - O(n+m)
'''
