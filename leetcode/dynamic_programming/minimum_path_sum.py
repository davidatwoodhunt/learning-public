from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        
        def minPathSumCalc(row, col):
            # If the cell is out of bounds, return infinity (invalid path)
            if row >= len(grid) or col >= len(grid[0]):
                return float('inf')
            
            # Base case: when we're at the bottom-right corner
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]
            
            # If this cell has already been calculated, return the cached value
            if (row, col) in memo:
                return memo[(row, col)]
            
            # Recursively compute the minimum path sum for both directions: down and right
            down = minPathSumCalc(row + 1, col)
            right = minPathSumCalc(row, col + 1)
            
            # Store the result in the memoization dictionary
            memo[(row, col)] = grid[row][col] + min(down, right)
            
            return memo[(row, col)]
        
        # Start the recursion from the top-left corner
        return minPathSumCalc(0, 0)

if __name__=='__main__':
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(solution.minPathSum(grid))
