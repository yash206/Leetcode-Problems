''' 
Question -
You are given an array words of size n consisting of non-empty strings.
We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].
For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].
Note that a string is considered as a prefix of itself.
'''

'''
Difficulty - Hard
'''


class Trie:
    def __init__(self):
        self.score = 0
        self.children = {}

    def add(self, s: str, i: int):
        if (i): self.score += 1
        if (i == len(s)): return
        if (not self.children.get(s[i])): self.children[s[i]] = Trie()
        self.children[s[i]].add(s, i+1)

    def dfs(self, s: str, i: int):
        if (i == len(s)): return self.score
        return self.score + self.children[s[i]].dfs(s, i+1)
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word, 0)
        res = []
        for word in words:
            res.append(trie.dfs(word, 0))
        return res
        


'''
Time Complexity - O(n*m)
'''
