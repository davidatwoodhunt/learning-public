from typing import List 
import pprint
class Solution:
    def canPartition(self, nums:List[int],target:int) ->bool:

        dp = [[False for _ in range(target+1)] for _ in range(len(nums)+1)]
        for i in range(1,len(nums)+1):
            for j in range(target+1):
                if j == 0:
                    dp[i-1][j] = True #set at start
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[len(nums)][target]


if __name__=="__main__":
    nums = [2,3,7,8,10]
    target = 11
    s = Solution()
    print(s.canPartition(nums,target)) # True