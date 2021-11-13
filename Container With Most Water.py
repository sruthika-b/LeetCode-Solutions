class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxi = 0
        a = 0
        b = len(height)-1
        while a<b:
            ai = min(height[a],height[b])
            wi = b-a
            maxi = max(maxi, ai*wi)
            if ai==height[a]:
                a+=1
            else:
                b-=1
        return maxi
            
            
        
