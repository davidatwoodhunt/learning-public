from pprint import pprint
class Solution:

    def longestCommonSubsequence(self,text1:str,text2:str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        # have the zero cases here so that's why +1
        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1]
                  
                    )
        return dp[len(text2)][len(text1)]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("abcde","ace")) # 3
    print(s.longestCommonSubsequence("abc","abc")) # 3