class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')' : '(', "]" : "[", "}" : "{"}

        for char in s:
            if char not in matching: #if this is an open parenthesis
                stack.append(char)
            
            if char in matching:
                if not stack or matching[char] != stack[-1]:
                    return False
                stack.pop()
        
        return not stack