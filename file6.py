<<<<<<< HEAD
# Simple Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Dictionary of functions
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nAvailable operations: add, subtract, multiply, divide")
    choice = input("Enter operation: ").lower()

    if choice in operations:
        result = operations[choice](num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid operation selected.")

except ValueError:
    print("Please enter valid numbers.")
=======
import json


def save_config(data: dict, filename: str):
    """Save dictionary data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_config(filename: str) -> dict:
    """Load and return data from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)


def update_config(filename: str, key: str, value):
    """Update a key in the JSON config file and save it."""
    config = load_config(filename)
    config[key] = value
    save_config(config, filename)


# json.dump() writes JSON data directly to a file.
# json.dumps() converts Python objects into a JSON string.


# Test Configuration
config_data = {
    "model": "LinearRegression",
    "learning_rate": 0.01,
    "epochs": 10
}

# Save config
save_config(config_data, "config.json")

# Load config
print("Original Config:")
print(load_config("config.json"))

# Update epochs
update_config("config.json", "epochs", 20)

print("\nUpdated Config:")
print(load_config("config.json"))
>>>>>>> master
