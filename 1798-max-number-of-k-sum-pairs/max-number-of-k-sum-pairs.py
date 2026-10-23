class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i=0
        j=len(nums)-1
        counter=0
        nums.sort()
        while(i<j):
            x=nums[i]+nums[j]
            if x==k:
                counter+=1
                i+=1
                j-=1
            else:
                if x>k:
                    j-=1
                else:
                    i+=1
        return counter
            
