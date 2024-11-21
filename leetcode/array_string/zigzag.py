

class Solution:
    def convert(self,s, numRows):
        if numRows == 1:
            return s
        res = ['' for i in range(numRows)]
        index = 0
        step = 1
        for i in s:
            res[index] += i
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(res)

def main():
    s = "AB"
    numRows = 1
    S = Solution()
    print(S.convert(s, numRows))

if __name__ == '__main__':
    main()