class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        arr = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        # print(arr)
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

        # for i in range(m):
        #     for p in range(n):
        #         print(arr[i][p])

        return arr[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]