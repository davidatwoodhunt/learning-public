from typing import List, Tuple
#Problem:
#You are a professional robber planning to rob houses along a street. 
#Each house has a certain amount of money stashed, 
#the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
#and it will automatically contact the police if two adjacent houses were broken into on the same night.
#Given an integer array nums representing the amount of money of each house,
#return the maximum amount of money you can rob tonight without alerting the police.
class Solution:
    def __init__(self):
        self.memo = []
        
    def priv_rob(self,nums:List[int], index:int) -> int:
        if index <0:
            return 0
        if self.memo[index] >=0:
            return self.memo[index]
        else:
            # This works since you either can rob the house and take the loot or pass 
            # so if you take it, you are restricted in that house and the one adjacent, starting from the end 
            # you are restricted only in the house you are in and the one adjacent to it
            # so you can either rob the house and the one two houses before or
            # you can pass and rob the house before but not get the loot from the house you are in
            best = max(
                self.priv_rob(nums,index-1), # pass
                self.priv_rob(nums,index-2) + nums[index] # take the loot
            )
            self.memo[index] = best
            
            return best
    def rob(self, nums: List[int]) -> int:
        self.memo = [-1]*(len(nums)+1)
        return self.priv_rob(nums,len(nums)-1)
            

