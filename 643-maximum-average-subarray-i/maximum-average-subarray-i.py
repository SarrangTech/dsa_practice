class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sm=sum(nums[:k])
        avg=sm/k
        mx=avg
        for right in range(k,len(nums)):
            sm+=nums[right]
            sm-=nums[right-k]
            avg=sm/k
            if avg>mx:
                mx=avg
        return mx

            
        