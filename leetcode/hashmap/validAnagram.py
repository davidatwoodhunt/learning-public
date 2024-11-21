#!/usr/bin/env python
# coding: utf-8

# # Valid Anagram 
# 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# In[5]:


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        anagram_map = {}
        for c in s:
            if c not in anagram_map.keys():
                anagram_map[c] = 1
            else:
                anagram_map[c] +=1
        for c in t:
            if c not in anagram_map.keys():
                return False
            else:
                if anagram_map[c] <= 0:
                    return False
                else:
                    anagram_map[c] -=1
        return True 


# In[8]:


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
    print(s.isAnagram("a", "ab"))
    print(s.isAnagram("a", "a"))
    print(s.isAnagram("a", "b"))


# In[ ]:





# In[ ]:




