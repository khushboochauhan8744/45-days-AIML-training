# Day 1 Extended Intro

name = "Khushbu"
age = 18
city = "Gurgaon"
favorite_subject = "Data Analytics"
target_role = "Data Analyst"

student = {
    "name": name,
    "age": age,
    "city": city,
    "favorite_subject": favorite_subject,
    "target_role": target_role
}

print(f"My name is {student['name'].title()}.")
print(f"I am {student['age']} years old.")
print(f"I live in {student['city'].upper()}.")
print(f"My favorite subject is {student['favorite_subject']} and I want to become a {student['target_role'].lower()}.")