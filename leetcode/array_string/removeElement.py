class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = sum([1 for x in nums if x ==val])
        for _,i in enumerate(nums):
            if i == val:
                #switch with first one non equal to the val at the back
                switch_idx = len(nums)-1
                while nums[switch_idx] == val:
                    switch_idx -=1
                if switch_idx > _:
                    nums[_] = nums[switch_idx]
                    nums[switch_idx] =val
        return count

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    s = Solution()
    print(s.removeElement(nums, val))
    print(nums)