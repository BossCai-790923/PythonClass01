'''
快速copy 过去，大致讲解下
和范老师的0361一样。代码写得也是非常的干净

'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        arr = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        arr[0][0] = 1

        if obstacleGrid[0][0] == 1:
            arr[0][0] = 0

        for i in range(len(obstacleGrid)):
            for p in range(len(obstacleGrid[i])):
                if obstacleGrid[i][p] == 1:
                    continue
                if i > 0:
                    arr[i][p] += arr[i - 1][p]
                if p > 0:
                    arr[i][p] += arr[i][p - 1]

        return arr[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]