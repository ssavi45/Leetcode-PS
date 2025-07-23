# for given integer x, return True if the number is palindrome, False otherwise

class solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        
        for i in range(n // 2):
            if x[i] != x[n-1-i]:
                return False
        return True
            
sol = solution()
print(sol.isPalindrome(-121))
print(sol.isPalindrome(121))
print(sol.isPalindrome(10))
print(sol.isPalindrome(0))