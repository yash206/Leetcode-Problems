''' 
Question -
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].
For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
Return an array answer where answer[i] is the answer to the ith query.
'''

'''
Difficulty - Medium
'''


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Compute prefix XOR
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]
        
        # Process each query
        print(prefix)
        result = []
        for l, r in queries:
            if l == 0:
                result.append(prefix[r])
            else:
                result.append(prefix[r] ^ prefix[l - 1])
        
        return result


'''
Time Complexity - O(n+q)
'''
