# Skills Counter

skills = ["Python", "SQL", "Excel", "Graphic Design", "Communication"]

for number, skill in enumerate(skills, start=1):
    print(f"{number}. {skill}")

print(f"\nTotal skills: {len(skills)}")