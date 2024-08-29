''' 
Question -
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
'''

'''
Difficulty - Medium
'''


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graphX = defaultdict(list)
        graphY = defaultdict(list)
        for x,y in stones:
            graphX[x].append(y)
            graphY[y].append(x)
        connectedComponent = 0
        visited = set()
        for x,y in stones:
            if (x,y) not in visited:
                q = deque([(x,y)])
                while q:
                    xo,yo = q.popleft()
                    if (xo,yo) not in visited:
                        visited.add((xo,yo))
                        for neiY in graphX[xo]:
                            q.append((xo,neiY))
                        for neiX in graphY[yo]:
                            q.append((neiX,yo))
                connectedComponent += 1
        
        return len(stones)-connectedComponent



'''
Time Complexity - O(n)
'''
