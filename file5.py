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