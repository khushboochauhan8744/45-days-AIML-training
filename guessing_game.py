<<<<<<< HEAD
# Number Guessing Game

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!\n")

        elif guess > secret_number:
            print("Too high!\n")

        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

        remaining = max_attempts - attempts
        print(f"Attempts left: {remaining}\n")

    except ValueError:
        print("Please enter a valid number.\n")

# Runs only if the loop ends without break
else:
    print(f"Game Over! The correct number was {secret_number}.")
<<<<<<< HEAD:file8.py
=======
import csv


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self) -> float:
        return sum(product.price * product.quantity for product in self.products)

    def find_product(self, name: str):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["name", "price", "quantity"])

            for product in self.products:
                writer.writerow([
                    product.name,
                    product.price,
                    product.quantity
                ])

    def load_from_csv(self, filename):
        self.products = []

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                product = Product(
                    row["name"],
                    float(row["price"]),
                    int(row["quantity"])
                )
                self.products.append(product)


# Create Inventory
inventory = Inventory()

# Add Products
inventory.add_product(Product("Laptop", 50000, 2))
inventory.add_product(Product("Mouse", 500, 10))
inventory.add_product(Product("Keyboard", 1200, 5))

# Total Value
print("Total Inventory Value:", inventory.total_value())

# Search Product
product = inventory.find_product("laptop")
print("Found Product:", product)

# Save to CSV
inventory.save_to_csv("inventory.csv")
print("Inventory saved to inventory.csv")

# Load from CSV
new_inventory = Inventory()
new_inventory.load_from_csv("inventory.csv")

print("\nProducts Loaded From CSV:")
for product in new_inventory.products:
    print(product)


# Explore:
# @staticmethod does not receive self or cls automatically.
# A static method behaves like a normal function inside a class.
#
# load_from_csv() can be a class method if it creates and returns
# a new Inventory object using cls().
# As an instance method, it loads data into an existing Inventory object.
>>>>>>> master
=======
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7:guessing_game.py
