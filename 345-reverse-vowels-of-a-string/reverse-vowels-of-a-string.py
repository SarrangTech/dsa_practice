class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        vowels=['a','e','i','o','u']
        st=list(s)
        while(i<j):
            if st[i].lower() in vowels and st[j].lower() in vowels:
                st[i],st[j]=st[j],st[i]
                i+=1
                j-=1
            elif st[j].lower() not in vowels:
                j-=1
            else:
                i+=1
        return "".join(st)


        