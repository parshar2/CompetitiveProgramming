class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        paths = [0]*len(obstacleGrid)
        paths[0] = 1
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j]:
                paths[0] = 0
            for i in range(1, len(obstacleGrid)):
                if obstacleGrid[i][j]:
                    paths[i] = 0
                else:
                    paths[i] = paths[i] + paths[i-1]
        return paths[len(obstacleGrid) -1]