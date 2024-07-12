def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

a = float(input("Enter the numerator: "))
b = float(input("Enter the denominator: "))
print(f"Result: {safe_divide(a, b)}")
