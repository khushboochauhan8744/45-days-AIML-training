import csv

# Create students.csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "math", "science", "english"])
    writer.writerow(["Khushbu", 85, 90, 88])
    writer.writerow(["Mansi", 75, 80, 70])
    writer.writerow(["Riya", 60, 65, 55])

# Read students.csv and create results.csv

with open("students.csv", "r") as infile:
    reader = csv.DictReader(infile)

    with open("results.csv", "w", newline="") as outfile:
        fieldnames = ["name", "average", "grade"]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            avg = (
                int(row["math"]) +
                int(row["science"]) +
                int(row["english"])
            ) / 3

            if avg >= 90:
                grade = "A"
            elif avg >= 75:
                grade = "B"
            elif avg >= 60:
                grade = "C"
            elif avg >= 40:
                grade = "D"
            else:
                grade = "F"

            writer.writerow({
                "name": row["name"],
                "average": round(avg, 2),
                "grade": grade
            })

print("results.csv created successfully!")