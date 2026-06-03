from typing import Optional


def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """
    Returns the division of two numbers.
    Returns None if the denominator is zero.
    """
    if b == 0:
        return None
    return a / b


def power(base: float, exp: float) -> float:
    """
    Returns the result of base raised to the power exponent.
    """
    return base ** exp


def modulo(a: int, b: int) -> int:
    """
    Returns the remainder after division.
    Returns 0 if division by zero is attempted.
    """
    if b == 0:
        print("Error: Cannot perform modulo by zero.")
        return 0
    return a % b


# Test Cases
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Division by Zero:", divide(10, 0))
print("Power:", power(2, 3))
print("Modulo:", modulo(10, 3))
print("Modulo by Zero:", modulo(10, 0))