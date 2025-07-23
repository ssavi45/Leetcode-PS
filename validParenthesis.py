class solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket:
                top = stack.pop() if stack else '#'
                if bracket[char] != top:
                    return False
            else:
                stack.append(char)
                
        return not stack
    
sol = solution()
print(sol.isValid("()"))            #True
print(sol.isValid("()[]{}"))        #True
print(sol.isValid("(]"))            #False
print(sol.isValid("([])"))          #True
print(sol.isValid("([)]"))          #False
print(sol.isValid(")()({[]}()]["))  #False