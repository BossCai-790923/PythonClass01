class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        x = len(obstacleGrid)
        y = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        for i in range(x):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = -1
            else:
                break

        for j in range(1, y):
            if obstacleGrid[0][j] == 0:
                obstacleGrid[0][j] = -1
            else:
                break

        print(obstacleGrid)

        for i in range(1, x):
            for j in range(1, y):
                if obstacleGrid[i][j] == 0:
                    if obstacleGrid[i - 1][j] < 0:
                        obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                    if obstacleGrid[i][j - 1] < 0:
                        obstacleGrid[i][j] += obstacleGrid[i][j - 1]

        return -obstacleGrid[-1][-1]

s = Solution()
grid = [[0,0,0],[0,1,0],[0,0,0]]
answer = s.uniquePathsWithObstacles(grid)
print(answer)