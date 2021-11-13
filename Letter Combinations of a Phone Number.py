class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        
        queue = [i for i in mapping[digits[0]]]
        for i in range(1,len(digits)):
            new_queue = []
            while queue:
                element = queue.pop(0)
                for j in mapping[digits[i]]:
                    new_queue.append(element+j)
            queue = new_queue
        return queue
                    
        
