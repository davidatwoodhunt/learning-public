#!/usr/bin/env python
# coding: utf-8

# In[43]:


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_map = {}

        for a,b in zip(s,t):
            if a in iso_map.keys():
                if iso_map[a]!= b:
                    return False
            if b in iso_map.values():
                if a not in iso_map.keys():
                    return False 
            else:
                iso_map[a]=b
        return True 


# In[44]:


if __name__ == '__main__':
    print(Solution().isIsomorphic("egg", "add"))
    print(Solution().isIsomorphic("foo", "bar"))
    print(Solution().isIsomorphic("badc", "baba"))


# In[ ]:




