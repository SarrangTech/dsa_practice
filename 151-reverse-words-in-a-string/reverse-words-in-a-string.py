class Solution:
    def reverseWords(self, s: str) -> str:
        li=s
        li=li.split(' ')
        li=[i for i in li if i!='']
        i=0
        j=len(li)-1
        while(i<j):
            li[i],li[j]=li[j],li[i]
            i+=1
            j-=1
        return " ".join(li)
        