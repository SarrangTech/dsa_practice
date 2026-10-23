class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        match=0
        while(i<len(s) and j<len(t)):
            if s[i]==t[j]:
                match+=1
                i+=1
                j+=1
            else:
                j+=1
        return match==len(s)



        