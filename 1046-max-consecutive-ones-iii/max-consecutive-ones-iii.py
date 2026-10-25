class Solution(object):
    def longestOnes(self, nums, k):
        left=0
        right=0
        reserve=k
        length=0
        mx=0
        for right in range(0,len(nums)):
            if nums[right]==0:
                reserve-=1

            while(reserve<0):
                if nums[left]==0:
                    reserve+=1
                left+=1
            
            mx = max(mx, right - left + 1)
        return mx



        