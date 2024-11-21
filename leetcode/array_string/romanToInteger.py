#!/usr/bin/env python
# coding: utf-8

# # Roman To Int
# ### Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# ```
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# ```
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# 
# I can be placed before V (5) and X (10) to make 4 and 9.  
# X can be placed before L (50) and C (100) to make 40 and 90.  
# C can be placed before D (500) and M (1000) to make 400 and 900.  
# ### Given a roman numeral, convert it to an integer. 
# 
# 

# In[28]:


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        edge_cases = {
            "IV":4,
            "IX":9,
            "XL": 40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        number = 0
        idx = 0
        while idx < len(s):
            d_slice = s[idx:idx+2]
            one_slice = s[idx:idx+1]
            if d_slice in edge_cases:
                number += edge_cases[d_slice]
                idx += 2 # add another one to compensate 
            else:
                number += roman_dict[one_slice]
                idx += 1 
        return number 


# # Notes:
# - This solution worked but you can also view the prefix as a subtraction on this instead of an edge case
#   - in the case where there is a valid prefix, then all you would need to do is subtract the prefix from the number and then add that number to your result
#   - probably saves on hard coding but doesn't seems any _more_ memory efficient 

# In[31]:


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
    print(s.romanToInt("I"))
    print(s.romanToInt("II"))
    print(s.romanToInt("V"))
    print(s.romanToInt("X"))
    print(s.romanToInt("L"))
    print(s.romanToInt("C"))
    print(s.romanToInt("D"))
    print(s.romanToInt("M"))
    print(s.romanToInt("MMMCMXCIX"))
    print(s.romanToInt("MMMCMXCIV"))
    print(s.romanToInt("MMMCMXCIII"))
    print(s.romanToInt("MMMCMXCII"))
    print(s.romanToInt("MMMCMXCI"))


# In[ ]:




