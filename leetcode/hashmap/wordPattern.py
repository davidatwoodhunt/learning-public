#!/usr/bin/env python
# coding: utf-8

# # Word Pattern
# 
# - Given a pattern and a string s, find if s follows the same pattern.
# - Here follow means a full match, such that there is a _bijection_ between a letter in pattern and a _non-empty_ word in s.

# In[49]:


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # mapping exercise 
        p_list = list(pattern)
        s_list = s.split(" ")
        if len(p_list) != len(s_list): return False 
        bijection = {}
        for p,str in zip(p_list,s_list):
            #print(p, str)
            if p not in bijection.keys():
                if str in bijection.values():
                    return False 
                bijection[p] = str
            if bijection[p] != str:
                return False
        return True 

        


# In[50]:


if __name__ == '__main__':
    pattern = "abba"
    strs = "dog cat cat dog"
    s = Solution()
    print(s.wordPattern(pattern,strs))
    pattern = "abba" 
    strs = "dog cat cat fish"
    print(s.wordPattern(pattern,strs))
    strs ="dog dog dog dog"
    print(s.wordPattern(pattern,strs))


# In[ ]:





# In[ ]:




