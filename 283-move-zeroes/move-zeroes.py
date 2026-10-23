class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums)==1:
            return nums
        i=0
        j=1
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        

            
