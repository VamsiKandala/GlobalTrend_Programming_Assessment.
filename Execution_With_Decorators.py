import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@time_logger
def computationally_expensive_task(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

n = int(input("Enter the number of iterations for the task: "))
print(f"Result: {computationally_expensive_task(n)}")
