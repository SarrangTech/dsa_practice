class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer=[1]*n
        left=1
        for i in range(0,len(nums)):
            answer[i]=left
            left*=nums[i]
        right=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=right
            right*=nums[i]
        return answer

    





                
        