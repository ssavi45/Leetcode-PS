def fib_bottom_up(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    bottom_up = [0] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

print(f"fib(0) = {fib_bottom_up(0)}")
print(f"fib(1) = {fib_bottom_up(1)}")
print(f"fib(2) = {fib_bottom_up(2)}")
print(f"fib(3) = {fib_bottom_up(3)}")
