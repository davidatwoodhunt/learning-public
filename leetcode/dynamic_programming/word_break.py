from typing import List
from functools import cache
import logging
logging.basicConfig(level=logging.DEBUG)
class Solution:
    def wordBreak_recursive(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        #TODO lookuptable
        @cache
        def find_by_dp(index):
            if index <0:
                return True
            for word in word_set:
                if (s[index-len(word)+1:index+1] in wordDict and 
                    find_by_dp(index-len(word))
                    ):
                    return True
            return False
        return find_by_dp(len(s)-1)
    
    def wordBreak(self, s:str, wordDict:List[str]) -> bool:
        ### iterative method using lookuptable
        lookup_table = [False] * (len(s)+1) # last bit handles the whole word
        lookup_table[0] = True # empty string
        word_set = set(wordDict)
        for i in range(1,len(s)+1):
            for j in range(i):
                logging.debug(f"i:{i}, j:{j}, s[j:i]:{s[j:i]}")
                if lookup_table[j] and s[j:i] in word_set:
                    logging.debug(f"found word: {s[j:i]}, Done")
                    lookup_table[i] = True
                    break # only need to break once we've found it 
            logging.debug(f"lookup_table [{i}], {lookup_table[i]}")
        logging.debug(lookup_table)
        return lookup_table[len(s)]

if __name__ == "__main__":
    solution = Solution()
    solution.wordBreak("leetcode", ["leet","code"])
                
