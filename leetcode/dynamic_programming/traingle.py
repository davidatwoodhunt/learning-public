from typing import List
from functools import cache

class Solution:
    def minimumTotal_recursive(self, triangle: List[List[int]]) -> int:
        # to be sure you need to evaluate EVERY sub path 
            # There is a way of optimizing this to trim the amount of paths
        # start at the top 
        # for the same node, index has to be equal in both layers or +1 in layer 2
        @cache
        def dfs(i,j):
            if i == len(triangle):
                return 0 # at the bottom
            lower_left = triangle[i][j] + dfs(i+1,j) #index same
            lower_right = triangle[i][j] + dfs(i+1,j+1) # index +1
            return min(lower_left,lower_right)
        return dfs(0,0)

    def minimumTotal_iterative(self,triangle: List[List[int]]) -> int:
        #TODO DP table 
        # start at the bottom  and we can store the results from the intermediate paths

        n = len(triangle) # have the width of the base of the triangle
        dp = [[-1] * n for _ in range(n)]
        dp[n-1] = triangle[n-1] #initialize the last row as the values of the last row of the triangle
        #print(dp)

        for i in range(n-2,-1,-1): #go up start at the second to last layer
            
            for j in range(i+1): #go down
                lower_left = triangle[i][j] + dp[i+1][j]
                lower_right = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(lower_left,lower_right)
            #print(i,dp)
        
        #print(dp)
        
        return dp[0][0]

    def minimumTotal(self,triangleList: List[List[int]]) -> int:
        return self.minimumTotal_iterative(triangleList)

if __name__ == '__main__':
    solution = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(solution.minimumTotal(triangle))