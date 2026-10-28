class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals=sorted(intervals)
        result=[intervals[0][:]]
        for start,end in intervals[1:]:
            if start<=result[-1][1]:
                result[-1][1]=max(end,result[-1][1])
            else:
                result.append([start,end])
        return result


            
