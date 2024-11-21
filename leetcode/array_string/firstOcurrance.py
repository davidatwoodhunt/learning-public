#!/usr/bin/env python
# coding: utf-8

# # Find the Index of the First Occurrence in a String
# 
# - Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# In[1]:


class Solution:
    def firstOcurrance(self, haystack: str, needle: str) -> int:
        first_idx = -1
        len_str = len(needle)
        for i in range(0,len(haystack)):
            sub_str = haystack[i:i+len_str]
            if sub_str == needle:
                return i
        return first_idx


# In[2]:


if __name__ == '__main__':
    s = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(s.strStr(haystack,needle))
    haystack = "leetcode"
    needle = "leeto"
    print(s.strStr(haystack,needle))


# In[ ]:





# In[ ]:




