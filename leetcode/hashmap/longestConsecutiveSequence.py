from typing import List 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = {}
        if len(nums)==0:return 0
        for i in range(len(nums)):
            res[nums[i]] = i
        lst = sorted(res.keys(),reverse=True)
        longest = 1
        count = 1
        for i in range(len(lst)-1):
            if lst[i+1] == lst[i]-1:
                count+=1
                if count > longest:
                    longest = count
            else:
                count = 1
        return longest
