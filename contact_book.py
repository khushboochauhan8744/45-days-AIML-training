# Mini Contact Book

contacts = [
    {
        "name": "Alex",
        "phone": "9876543210",
        "email": "alex@email.com"
    },
    {
        "name": "Khushbu",
        "phone": "9123456780",
        "email": "khushbu@email.com"
    },
    {
        "name": "Riya",
        "phone": "9988776655",
        "email": "riya@email.com"
    },
    {
        "name": "Aman",
        "phone": "9871234567",
        "email": "aman@email.com"
    },
    {
        "name": "Sneha",
        "phone": "9001122334",
        "email": "sneha@email.com"
    }
]


def find_contact(name):
    # Case-insensitive comparison using lower()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return "Contact not found."


# User input
search_name = input("Enter contact name: ")

result = find_contact(search_name)

print("\nSearch Result:")

if isinstance(result, dict):
    print(f"Name: {result['name']}")
    print(f"Phone: {result['phone']}")
    print(f"Email: {result['email']}")
else:
    print(result)
