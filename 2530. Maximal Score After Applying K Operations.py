''' 
Question -
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
In one operation:
choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.
The ceiling function ceil(val) is the least integer greater than or equal to val.
'''

'''
Difficulty - Medium
'''


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Create a max heap by pushing negative values (to simulate max heap)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        for _ in range(k):
            # Extract the largest element (invert the sign back to positive)
            max_elem = -heapq.heappop(max_heap)
            score += max_elem  # Add the value to the score
            
            # Compute the new value (ceil(max_elem / 3)) and push it back
            new_value = math.ceil(max_elem / 3)
            heapq.heappush(max_heap, -new_value)
        
        return score


'''
Time Complexity - O(n*log(n))
'''
