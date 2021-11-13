class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)            
            elif stack:
                if stack[-1]=="(" and i==")":
                    stack.pop()
                elif stack[-1]=="{" and i=="}":
                    stack.pop()
                elif stack[-1]=="[" and i=="]":
                    stack.pop()
                else:
                    return False  
            else:
                return False
        if len(stack)==0:
            return True
        return False
                    
        
