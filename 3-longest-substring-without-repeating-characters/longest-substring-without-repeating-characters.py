class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last={}
        best=0
        left=0
        for right,ch in enumerate(s):
            if ch in last and last[ch]>=left:
                left=last[ch]+1
            last[ch]=right
            best=max(best,right-left+1)
        return best
        