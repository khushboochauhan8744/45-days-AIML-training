<<<<<<< HEAD
# Word Frequency Counter

# collections.Counter can count words in one line:
# Counter(sentence.split())

def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


sentence = "Python is fun and Python is easy to learn"

result = word_frequency(sentence)

# Sort by frequency (highest to lowest)
sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)

print("Word Frequency:\n")

for word, count in sorted_result:
    print(f"{word}: {count}")
<<<<<<< HEAD:file5.py
=======
class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self):
        return (f"Book: {self.title}, Author: {self.author}, "
                f"Year: {self.year}, Pages: {self.pages}")


class EBook(LibraryItem):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self):
        return (f"EBook: {self.title}, Author: {self.author}, "
                f"Year: {self.year}, File Size: {self.file_size_mb} MB")


# Create 2 Book objects
book1 = Book("Python Programming", "John Doe", 2022, 350)
book2 = Book("Data Structures", "Jane Smith", 2021, 420)

# Create 2 EBook objects
ebook1 = EBook("AI Basics", "David Lee", 2023, 15.5)
ebook2 = EBook("Machine Learning", "Sarah Khan", 2024, 10.2)

# Store all objects in one list
library_items = [book1, book2, ebook1, ebook2]

# Loop through and call describe()
for item in library_items:
    print(item.describe())

# Explore
print(isinstance(book1, LibraryItem))

# Output: True
# Explanation:
# Book inherits from LibraryItem, so a Book object
# is also considered a LibraryItem object.
>>>>>>> master
=======
>>>>>>> 6113c2d72fb694c6681db62e67215b85950297d7:word_frequency.py
