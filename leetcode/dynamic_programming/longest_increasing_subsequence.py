from typing import List
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # try recursive at first 
        if not len(nums): return 0
        sub = []
        for n in nums:
            if len(sub) == 0 or sub[-1] < n:
                sub.append(n)
            else:
                # binary search the largest elem
                idx= bisect_left(sub,n)
                sub[idx] = n

        return len(sub)

if __name__ == '__main__': 
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))