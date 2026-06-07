<<<<<<< HEAD
# Skills Counter

skills = ["Python", "SQL", "Excel", "Graphic Design", "Communication"]

for number, skill in enumerate(skills, start=1):
    print(f"{number}. {skill}")

print(f"\nTotal skills: {len(skills)}")
<<<<<<< HEAD:file2.py
=======
# 1. Extract numbers divisible by 3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

divisible_by_3 = [num for num in numbers if num % 3 == 0]
print("Divisible by 3:", divisible_by_3)


# 2. Words longer than 4 characters in title case

words = ["python", "code", "student", "java", "developer", "ai"]

long_words = [word.title() for word in words if len(word) > 4]
print("Long words:", long_words)


# 3. Celsius to Fahrenheit

celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Fahrenheit:", fahrenheit)


# 4. Flatten nested list

nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

flattened = [item for sublist in nested_list for item in sublist]
print("Flattened List:", flattened)


# Explore - Dictionary Comprehension

square_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary Comprehension:", square_dict)


# Explore - Set Comprehension

square_set = {x**2 for x in range(1, 6)}
print("Set Comprehension:", square_set)
>>>>>>> master
=======
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7:skills_counter.py
