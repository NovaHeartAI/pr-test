def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    # Test the calculator
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    print(f"10 / 2 = {divide(10, 2)}")
