#!/usr/bin/env python
# coding: utf-8

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# 
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# 
# 

# In[39]:


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p0 = 0
        p1 = 0
        while p1 < len(t) and p0 < len(s):
            #print(p0,p1,s,t)
            if s[p0] == t[p1]:
                p0 +=1
                p1 +=1
            else:
                p1 += 1
        if p0 == len(s):
            return True
        else:
            return False 


# In[41]:


s = Solution()
#Test case 1: Both strings are empty
assert s.isSubsequence("", "") == True
assert s.isSubsequence("abc", "ahbgdc") == True
assert s.isSubsequence("abc", "abcdef") == True
assert s.isSubsequence("abc", "adebfc") == True
assert s.isSubsequence("ace", "abcde") == True
#assert s.isSubsequence("abc", "ab") == False
#assert s.isSubsequence("abc", "ac") == False
#assert s.isSubsequence("abc", "bc") == False
#assert s.isSubsequence("abc", "c") == False
##assert s.isSubsequence("abc", "a") == False
#assert s.isSubsequence("abc", "b") == False
#assert s.isSubsequence("abc", "c") == False
#assert s.isSubsequence("abc", "ab") == False
#assert s.isSubsequence("abc", "bc") == False


# In[ ]:





# In[ ]:




