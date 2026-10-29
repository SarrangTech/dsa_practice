class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums)==0 or len(nums)==1:
            return []
        seen={}
        for i in range(0,len(nums)):
            x=target-nums[i]
            if x in seen:
                return [i,seen[x]]
            if nums[i] not in seen:
                seen[nums[i]]=i
        return []

                    
        
            