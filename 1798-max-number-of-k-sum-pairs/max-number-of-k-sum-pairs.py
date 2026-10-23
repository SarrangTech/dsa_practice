class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #brute force
        i=0
        j=len(nums)-1
        pairs=0
        nums.sort()
        while(i<j):
            x=nums[i]+nums[j]
            if x==k:
                pairs+=1
                j-=1
                i+=1
            elif x<k:
                i+=1
            else:
                j-=1
        return pairs
        