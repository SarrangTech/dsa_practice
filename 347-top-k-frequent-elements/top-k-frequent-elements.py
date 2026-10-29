from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums=Counter(nums)
        return sorted(nums,key=nums.get,reverse=True)[:k]
        