from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        return Fraction(
            self.numerator // common_divisor,
            self.denominator // common_divisor
        )

    def __str__(self):
        simplified = self.simplify()
        return f"{simplified.numerator}/{simplified.denominator}"

    def __add__(self, other):
        num = (self.numerator * other.denominator) + (
            other.numerator * self.denominator
        )
        den = self.denominator * other.denominator

        result = Fraction(num, den)
        return result.simplify()

    def __eq__(self, other):
        a = self.simplify()
        b = other.simplify()

        return (
            a.numerator == b.numerator and
            a.denominator == b.denominator
        )

    def __lt__(self, other):
        return (
            self.numerator * other.denominator <
            other.numerator * self.denominator
        )


# Test Pair 1
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print("Fraction 1:", f1)
print("Fraction 2:", f2)
print("Addition:", f1 + f2)
print("Less Than:", f1 < f2)
print()

# Test Pair 2
f3 = Fraction(2, 4)
f4 = Fraction(1, 2)

print("Fraction 3:", f3)
print("Fraction 4:", f4)
print("Equal:", f3 == f4)
print()

# Test Pair 3
f5 = Fraction(3, 5)
f6 = Fraction(4, 5)

print("Fraction 5:", f5)
print("Fraction 6:", f6)
print("Addition:", f5 + f6)
print("Less Than:", f5 < f6)

# Explore:
# @functools.total_ordering automatically generates
# the remaining comparison methods (__le__, __gt__, __ge__)
# if you define __eq__() and one ordering method such as __lt__().