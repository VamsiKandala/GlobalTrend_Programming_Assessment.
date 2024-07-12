def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the position of the Fibonacci number to compute: "))
print(f"The {n}th Fibonacci number is {fibonacci(n)}")
