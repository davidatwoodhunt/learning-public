#!/usr/bin/env python
# coding: utf-8

# # Longest Common Prefix
# - Find longest common prefix and return empty string if there are none 
# - 

# In[8]:


from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        for p in range(min([len(x) for x in strs])):
            starter_letter = strs[0][p]
            prefix_add = True
            for s in strs:
                letter = s[p]
                if letter != starter_letter:
                    prefix_add = False
            if prefix_add:
                longest_prefix += starter_letter
            else:
                break 
        return longest_prefix


# In[9]:


if __name__ == '__main__':
    s = Solution()
    strs =["cir","car"]
    print(s.longestCommonPrefix(strs))
    strs =["a"]
    print(s.longestCommonPrefix(strs))
    strs =["flower","flow","flight"]
    print(s.longestCommonPrefix(strs))
    strs =["dog","racecar","car"]
    print(s.longestCommonPrefix(strs))


# In[ ]:





# In[ ]:




