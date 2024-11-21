
class Solution:
    def minDistance(self, text1:str,text2:str)->int:
        dp = [[0 for n in range(len(text1)+1)] for _ in range(len(text2)+1)]

        # Initialize the first row (number of insertions needed to transform empty string into text1)
        for i in range(len(text1) + 1):
            dp[0][i] = i  # Inserting i characters into empty string

        # Initialize the first column (number of deletions needed to transform text2 into empty string)
        for j in range(len(text2) + 1):
            dp[j][0] = j  # Deleting j characters from text2 to make it an empty string

        for i in range(1,len(text2)+1):
            #initalize 
            for j in range(1,len(text1)+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1
        return dp[len(text2)][len(text1)]

