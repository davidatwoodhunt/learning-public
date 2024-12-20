#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
#You may assume that you have an infinite number of each kind of coin.

from typing import List
import math 
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        print(f'Calling coinChange with coins: {coins}, amount: {amount}')
        dp =[math.inf] * (amount + 1) #handle last case 
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1): # why coin 
                if i - coin >= 0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return -1 if dp[-1] == math.inf else dp[-1]



