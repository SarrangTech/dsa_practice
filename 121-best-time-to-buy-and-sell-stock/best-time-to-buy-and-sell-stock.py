class Solution(object):
    def maxProfit(self, prices):
        best=0
        lowest=float('inf')
        for price in prices:
            best=max(best,price-lowest)
            lowest=min(lowest,price)
        return best
