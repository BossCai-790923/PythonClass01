
'''
https://leetcode.com/problems/unique-paths-ii
'''


'''
ANALYSIS


---------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array? 
---------------------------------------------------------------------------------
Original Q: How many possible unique paths are there?
Parameterzied the Q: How many possible unique paths are there when the robot is at row n and column m?

f(m,n):
param m : row m
param n : column n
f(m,n)  : total unique path

dp = [i][j]:
index i : row i
index j : column j
dp[i][j]  : total unique path

---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------
dp = np.full([m,n], -1, dtype=np.int32)

[base case]
For the 1st row, there is only 1 possible path before we meet any obstacle. And there is 0 possible path after the 1st obstacle.
For the 1st column, there is only 1 possible path before we meet any obstacle. And there is 0 possible path after the 1st obstacle.
<We need to use some complex logic here> 


------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to subproblem?
------------------------------------------------------------------------

Because the robot can ony move rightwards and downwards, so for position dp[i][j], the value is:

dp[i][j] = dp[i-1][j] + dp[i][j-1]   when obstacleGrid[i][j] == 0  
dp[i][j] = 0                         when obstacleGrid[i][j] == 1  
'''

import numpy as np

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        row_count = len(obstacleGrid)
        column_count = len(obstacleGrid[0])

        # define dp array
        dp = np.full([row_count, column_count], -1, dtype=np.int32)

        # init dp array
        obstacleMet = False
        for i in range(column_count):
            if obstacleGrid[0][i] == 1: # Obstacle met!
                obstacleMet = True
            dp[0,i] = 0 if obstacleMet else 1 # single line if / else

        obstacleMet = False
        for i in range(row_count):
            if obstacleGrid[i][0] == 1: # Obstacle met!
                obstacleMet = True
            dp[i,0] = 0 if obstacleMet else 1 # single line if / else


        for i in range(1, row_count):
            for j in range(1, column_count):
                if obstacleGrid[i][j] == 1:
                    dp[i,j] = 0
                else:
                    dp[i,j] = dp[i-1,j] + dp[i,j-1]

        return dp[row_count -1][column_count-1]



# --Testing code -------------------------------
s = Solution()
grid = [[0,0,0],[0,1,0],[0,0,0]]
print(s.uniquePathsWithObstacles(grid))
