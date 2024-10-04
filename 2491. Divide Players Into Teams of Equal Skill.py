''' 
Question -
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
The chemistry of a team is equal to the product of the skills of the players on that team.
Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
'''

'''
Difficulty - Medium
'''


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort the skills
        skill.sort()
        
        # Total skill of each team
        target_sum = skill[0] + skill[-1]
        
        total_chemistry = 0
        n = len(skill)
        
        # Try to pair the players with the same total skill
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target_sum:
                return -1  # If any pair doesn't match the target sum, return -1
            # Add the product (chemistry) of this team
            total_chemistry += skill[i] * skill[n - 1 - i]
        
        return total_chemistry


'''
Time Complexity - O(Nlogn)
'''
