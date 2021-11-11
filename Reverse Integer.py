class Solution:
    def reverse(self, x: int) -> int:
        if not str(x):
            return ''
        flag = 1
        start = 0
        if x<0:
            flag = -1
            start = 1
        x = str(x)[start:]
        x = x[::-1]
        res = flag*int(x)
        if res < -2**31 or res>((2**31)-1):
            return 0
        else:
            return res
            
            
        
