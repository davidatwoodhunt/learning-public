#!/usr/bin/env python
# coding: utf-8

# # Remove Duplicates II 
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# 
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# 
# Return k after placing the final result in the first k slots of nums.
# 
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# In[89]:


from typing import List 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 2
        for p0 in range(2,len(nums)):
            if nums[p0] != nums[p1-2]:
                nums[p1] = nums[p0]
                p1 +=1 
        return p1 


# ## Notes
#   - two pointer approach here, the key was to think of a slow and a fast pointer and then update
# ### Issues:
# - kept getting thrown by needing to _percolate_ upwards, but that wasn't necessary as what was in the end of the array doesn't matter 
# - much more importantly all you need to do is keep track of the _slow_ pointer 
# 
# ### annotation 
# - the solution starts at idx 2 since all that matters is the 2 and it is sorted in the first place 
#   - got the 2 -> len part of this correct 
#   - if the fast pointer -2 value is not equal to the slow pointer: then 

# In[90]:


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    sol = Solution()
    print(sol.removeDuplicates(nums)) # 2
    print(nums) # [1,1, 2]

    nums = [0,0,1,1,1,1,2,3,3]
    print(sol.removeDuplicates(nums)) # 2
    print(nums) # [1,1, 2]


# In[ ]:





# In[ ]:




