def fib(n):
    if n in (1, 2, 3):
        return 1
    else:
        return fib(n-1) + fib(n-2) + fib(n-3)
print(fib(int(input())))