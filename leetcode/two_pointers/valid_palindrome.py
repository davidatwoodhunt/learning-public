#!/usr/bin/env python
# coding: utf-8

# # Valid Palindrome 
# 
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# 

# In[40]:


class Solution:
    def isPalindrome(self, s: str) -> bool:
        LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        clean_string = "".join([c for c in s.upper() if c in LETTERS])
        if clean_string == "" or clean_string == " ": return True
        p1 = 0
        p2 = len(clean_string)-1
        is_pal = True
        while p1 < p2:
            if clean_string[p1] == clean_string[p2]:
                is_pal = True
            else:
                return False
            p1 +=1
            p2 -=1
        return is_pal 
        


# # Notes:
# - The trick here is edge case finding 
# - taking care that the first time you find an inequality then you can just say no without having to go back 
# 
# # Time and space complexity
# - Solution is going to run _O(n)_ in worst case 
#   - we do iterate over the string twice to clean it once and to find the palindrome _ness_ of it in second case
#     - however even worst case we're going half over the string $$ \mathcal{O} (\frac{n}{2}) + \mathcal{O} (2n) = \mathcal{O}(n) $$

# In[ ]:





# In[41]:


if __name__ == '__main__':
    s = Solution()
    valid_palindrome = s.isPalindrome
    s.isPalindrome(",; W;:GlG:;l ;,")
    assert valid_palindrome("") == True
    assert valid_palindrome("A man, a plan, a canal: Panama") == True
    assert valid_palindrome("race a car") == False
    assert valid_palindrome("level") == True
    assert valid_palindrome("12321") == True
    assert valid_palindrome("hello") == False
    assert valid_palindrome("a") == True
    assert valid_palindrome(",; W;:GlG:;l ;,") == False


# In[ ]:





# In[ ]:




