class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        left=1
        answer=[1]*n
        for i in range(0,len(nums)):
            answer[i]*=left
            left*=nums[i]
        right=1
        for i in range(n-1,-1,-1):
            answer[i]*=right
            right*=nums[i]
        return answer


    





                
        