

def calculate_and_print(a, b):
    """Calculates a - b and prints the result directly."""
    # Intentionally incorrect logic (subtraction instead of addition)
    difference_result = a - b
    # Output format is the same, but the value will be wrong (5 instead of 15)
    print(f"The result is: {difference_result}")

if __name__ == "__main__":
    x = 10
    y = 5
    # Call the function which now contains the bug and prints directly
    calculate_and_print(x, y)
