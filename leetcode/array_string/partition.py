class Solution(object):
    def is_palindrome(self,s):
        if len(s) == 1:
            return True
        return s[::-1] == s

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        pals = []
        #go into each possible partition
        for i in range(1,len(s)+1):
            if self.is_palindrome(s[:i]):
                if i == len(s):
                    pals.append([s[:i]])
                else:
                    for pal in self.partition(s[i:]):
                        pals.append([s[:i]]+pal)
        return pals
    
if __name__ == '__main__':
    s = "kayak"
    sol = Solution()
    print(sol.partition(s))