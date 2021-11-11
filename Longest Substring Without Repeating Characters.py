class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        i=0
        j=0
        maxi=0
        lis={}
        while i<j and j<len(s):
            c=s[i]
            if c in lis:
                if lis[c]<i:
                    maxi = max(maxi, (j-i))
                    lis[c] = i
                else:
                    i = j
                    lis[c] = j
            else:
                lis[c] = j
                    
            j+=1
            maxi = max(maxi,j-i)
        return maxi
