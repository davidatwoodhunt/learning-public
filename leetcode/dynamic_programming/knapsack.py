from typing import List
from pprint import pprint

class Solution:

    def knapsack(self, values:List[int], weights:List[int],capacity:int) -> int:
        n = len(values)
        dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

        for i in range(1,n+1):
            for w in range(capacity+1):
                if weights[i-1] <= w:
                    # we can add it 
                    dp[i][w] = max(
                        values[i-1] + dp[i-1][w-weights[i-1]],
                        dp[i-1][w]
                    )
                else:
                    # we cannot
                    dp[i][w] = dp[i-1][w]
        #pprint(dp)
        #print(n,capacity)
        return dp[n][capacity] # value at the end 


if __name__ == '__main__':
    values = [6,10,12]
    weights = [1,2,3]
    capacity = 5
    solution = Solution()
    solution.knapsack(values,weights,capacity)
