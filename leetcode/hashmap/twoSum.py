#!/usr/bin/env python
# coding: utf-8

# # Two Sum 
# 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.

# In[44]:


from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map sums to their incidies 
        complement_map = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in complement_map.keys():
                return [i,complement_map[comp]]
            else:
                complement_map[nums[i]] = i
                



# In[45]:


if __name__ =='__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
    print(s.twoSum([0, 4, 3, 0], 0))
    print(s.twoSum([-1, -2, -3, -4, -5], -8))


# # Notes
# - Think about this like a dynamic programming challenge, 
# - here the issue is that we're repeating a ton of calculations so the optimal strategy would be to check if we've already done the calc 

# In[ ]:





# In[ ]:





# In[ ]:




