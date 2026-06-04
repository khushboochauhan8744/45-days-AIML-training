import json

# JSON data as string
json_data = '''
{
    "name": "Khushbu",
    "role": "Python Intern",
    "skills": ["Python", "Git", "GitHub"]
}
'''

# Convert JSON string to Python dictionary
data = json.loads(json_data)

# List comprehension
skills = [skill.upper() for skill in data["skills"]]

# Print report
print(f"Name: {data['name']}")
print(f"Role: {data['role']}")
print(f"Skills: {', '.join(skills)}")