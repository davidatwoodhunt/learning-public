from typing import List 
class Solution:
    # two pointer method here, keep index of where we were on the overwrite and then just increment when we find something to replace it
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j +=1
        return j
        
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    print(s.removeDuplicates(nums))
    print(nums)