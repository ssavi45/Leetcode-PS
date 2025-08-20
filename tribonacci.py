#1137: N-th tribonacci number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        bottom_up = [0] * (n + 1)
        bottom_up[0] = 0
        bottom_up[1] = 1
        bottom_up[2] = 1
        
        for i in range(3, n + 1):
            bottom_up[i] = bottom_up[i-1] + bottom_up[i-2] + bottom_up[i-3]
        
        return bottom_up[n]

sol = Solution()
print(sol.tribonacci(25))  # Should output 44
