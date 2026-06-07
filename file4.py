<<<<<<< HEAD
# Tip Calculator

# return sends a value back from a function so it can be stored or reused.
# print only displays the value on the screen and does not send it back.

def calculate_tip(bill, tip_percent):
    tip_amount = bill * (tip_percent / 100)
    total_amount = bill + tip_amount

    return {
        "tip": tip_amount,
        "total": total_amount
    }


# Test 1
result1 = calculate_tip(1000, 10)
print(f"Bill: 1000 | Tip: {result1['tip']} | Total: {result1['total']}")

# Test 2
result2 = calculate_tip(750, 15)
print(f"Bill: 750 | Tip: {result2['tip']} | Total: {result2['total']}")

# Test 3
result3 = calculate_tip(500, 20)
print(f"Bill: 500 | Tip: {result3['tip']} | Total: {result3['total']}")
=======
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
>>>>>>> master
