# main.py (in hw1-p branch)
# Refactored: Calculation is wrapped in a function.
# The main block calls the function, receives the value, and prints it.

def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

if __name__ == "__main__":
    x = 10
    y = 5
    sum_result = add_numbers(x, y)
    # Output format remains the same for the action check
    print(f"The result is: {sum_result}") # Output should still be 15
