''' 
Question -
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
'''

'''
Difficulty - Medium
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        def helper(ind, t, ans, ds):
            if t == 0:
                ans.append(copy.deepcopy(ds))
                return
            prev = -1
            for i in range(ind, n):
                if prev == candidates[i]:
                    continue
                if candidates[i] > t:
                    break
                ds.append(candidates[i])
                helper(i+1, t-candidates[i], ans, ds)
                ds.remove(candidates[i])
                prev = candidates[i]

        ds = []
        ans = []
        helper(0, target, ans, ds)
        return ans


'''
Time Complexity - O(2ⁿ)
'''
