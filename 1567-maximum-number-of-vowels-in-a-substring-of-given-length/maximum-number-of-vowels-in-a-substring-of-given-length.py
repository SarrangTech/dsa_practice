class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        count=len([i for i in s[:k] if i in vowels])
        mx=count
        for right in range(k,len(s)):
            if s[right] in vowels:
                count+=1
            if s[right-k] in vowels:
                count-=1
            if count>mx:
                mx=count
        return mx
        