from typing import List

# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray
# whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # handle edge case 
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return len(nums)
        else:
            #sliding window aproach 
            
            left = 0
            result = float('inf')
            current_sum = 0
            for right in range(len(nums)):
                current_sum += nums[right]
                while current_sum >= target:
                    # keep growing the window if the sum is greater than or equal to target
                    result = min(result, right - left + 1)
                    current_sum -= nums[left]
                    left += 1
            return result if result != float('inf') else 0
            