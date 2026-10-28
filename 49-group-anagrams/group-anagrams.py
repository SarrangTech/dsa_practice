class Solution(object):
    def groupAnagrams(self, strs):
        di = {}
        for i in strs:
            x = "".join(sorted(i))

            if x not in di:
                di[x] = []

            di[x].append(i)

        return list(di.values())
        