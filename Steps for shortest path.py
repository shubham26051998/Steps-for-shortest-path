#!/usr/bin/env python
# coding: utf-8

# In[82]:


class cell:
    def __init__(self, x = 0, y = 0, dist = 0): 
        self.x = x 
        self.y = y 
        self.dist = dist 
          
# checks whether given position is inside the board 

def isInside(x, y, N): 
    if (x >= 1 and x <= N and y >= 1 and y <= N):  
        return True
    return False
      
# Method returns minimum step to reach destination

def minStepToReachTarget(startpos, finalpos, pawnpos, N): 
      
    #all possible movments for the knight 
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
      
    queue = []
    queue.append(cell(startpos[0], startpos[1], 0)) 
      
    # make all cell unvisited  
    visited = [[False for i in range(N + 1)] for j in range(N + 1)] 
      
    # mark starting state as visited 
    visited[startpos[0]][startpos[1]] = True
    
    while(len(queue) > 0): 
          
        t = queue[0] 
        queue.pop(0) 
          
        # if current cell is equal to target  
        # cell, return its distance  
        if(t.x == finalpos[0] and t.y == finalpos[1]): 
            return t.dist 
              
        # iterate for all reachable states  
        for i in range(8): 
              
            x = t.x + dx[i] 
            y = t.y + dy[i] 
              
            if(isInside(x, y, N) and not visited[x][y]):
                if (x != pawnpos[0] and y != pawnpos[1]):
                    visited[x][y] = True
                    queue.append(cell(x, y, t.dist + 1)) 
 
N = 8
startpos = [0, 0] 
finalpos = [7, 7]
print('Enter the pawn position')
pawnpos = list(int(i) for i in input().split())
res = minStepToReachTarget(startpos, finalpos, pawnpos, N)
if res:
    print('Steps required to reach destination:-',res)
else:
    print('No Possible paths.')

