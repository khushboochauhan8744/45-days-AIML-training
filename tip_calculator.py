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
