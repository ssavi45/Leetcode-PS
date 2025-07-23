# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

from typing import List

class solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        return [1] + [0] * n
            
    
sol = solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([4,3,2,2]))
print(sol.plusOne([9]))
print(sol.plusOne([0]))