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