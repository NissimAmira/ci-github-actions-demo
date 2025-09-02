def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def calculate_factorial(n):
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Factorial of 5: {calculate_factorial(5)}")