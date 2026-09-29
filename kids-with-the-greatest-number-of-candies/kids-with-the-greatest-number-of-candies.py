class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        bl=[0]*len(candies)
        mx=max(candies)
        for i in range(0,len(candies)):
            if (candies[i]+extraCandies)>=mx:
                bl[i]=True
            else:
                bl[i]=False
        return bl
