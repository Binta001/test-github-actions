#!/usr/bin/env python3
"""
Simple Calculator Application
A basic calculator with add, subtract, multiply, and divide operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    """Main function to run the calculator."""
    print("Welcome to Simple Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    
    # Example usage
    print(f"\n5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")

if __name__ == "__main__":
    main()
