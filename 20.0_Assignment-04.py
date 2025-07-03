'''
Background: AtliQ, a software-based service company, operates an internal library
to support the continuous learning and development of its employees. The library contains
various types of items, such as books and journals, available for borrowing.

Problem Statement: Celina, the librarian at AtliQ, currently handles the logistics of
borrowing and returning items manually, which includes managing the status of each item
and handling exceptions like borrowing attempts on items that are already loaned out.
Your task is to assist Celina by automating part of her workload by completing the following
tasks using Python.
'''

# Task 1: Implement the LibraryItem Class
'''
Scenario: Help Celina automate the borrowing and returning process for items in AtliQ's library.
Task: Create a Python class 'LibraryItem' with the following structure:
Attributes:
title: Name of the item. 
is_borrowed: Boolean, True if borrowed, False otherwise.
Methods:
borrow_item(): If is_borrowed is True, raise an exception
raise Exception(f"The item '{self.title}' is already borrowed.")
Otherwise, set is_borrowed to True.
return_item() should also have a similar logic.
'''


class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False  # default is not borrowed

    def borrow_item(self):
        if self.is_borrowed == True:  # check if the item is already borrowed
            raise Exception(f"The item {self.title} is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"The item {self.title} has been borrowed.")

    def return_item(self):
        if not self.is_borrowed:
            raise Exception(f"The item {self.title} is not borrowed, so it cannot be returned.")
        else:
            self.is_borrowed = False
            print(f"The item {self.title} has been returned and is now available for borrow.")

# Example usage and output
book1 = LibraryItem("Python Programming")
book2 = LibraryItem("The Magic of Thinking Big")
print(book2.title)
book2.borrow_item()
book2.return_item()
print()

# Title of book
print(book1.title)

# Borrow the book
book1.borrow_item()  # Output: The item 'Python programming' has been borrowed.

# Return the book
book1.return_item()  # Output: The item 'Python programming' has been returned and is now available for borrow.
print()

# Return the book again
# book.return_item()  # Output: Cannot return a book that it has not borrowed.
# Exception: The item 'Python programming' is not borrowed, so it can't be returned.

# Mistake I made: My code was modifying a local variable (is_borrowed) inside the methods, instead of modifying the
# object's attribute (self.is-borrowed).

# ####################################################################################################################

# Task 2: Create the Book Class
'''
Scenario: Celina at AtliQ's library needs to catalog books separately from other items to provide detailed information, 
including the authors' names.
Task: Develop a derived class Book from LibraryItem to manage books with additional details.
Details:
1. Attributes:
- Inherits all attributes from LibraryItem.
- author: Name of the book's author.
2. Implementation:
- Create an object of the Book class with:
    - title: "The Magic of Thinking Big"
    - author: "David Schwartz"
This will help Celina keep a more detailed inventory and enhance the library’s catalog system. 
'''

class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

book3 = Book("The Magic of Thinking Big", "David Schwatrz")
print(f"Title: {book3.title}, Author: {book3.author}")
print()

# #####################################################################################################################

# Task 3: Create the Journal Class
'''
Scenario: Celina needs to manage journals effectively in AtliQ's library, where each journal has specific issues
that are often requested by staff for their research and development work.
Task: Develop a derived class Journal from LibraryItem to manage journals with specific issue numbers.
Details:
1. Attributes:
    - Inherits all attributes from LibraryItem.
    - issue_number: The specific issue number of the journal.
2. Implementation:
    - Create an object of the Journal class with:
    - title: "Nature"
    - issue_number: 50
This setup will help Celina organize journals by issue number, making them easier to locate and manage.
'''
class Journal(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

book4 = Journal("Nature", 50)
print(f"Journal name: {book4.title}, Issue number: {book4.issue_number}")
print()

# #####################################################################################################################

# Task 4: Handle Borrowing Exceptions
'''
Scenario: Celina sometimes gets requests to borrow a book that’s already borrowed. To prevent this, we need to handle 
this situation in our code.
Task: Try borrowing the same book twice and handle the exception that occurs.
Details:
1. Process:
    - Use the Book object from Task 2.
    - Attempt to borrow the book two times in a row.
2. Exception Handling:
    - Catch the exception raised when trying to borrow it the second time.
    - Print the exception message.
This will help Celina prevent errors when someone tries to borrow an already borrowed book.
'''

try:
    book1.borrow_item()
    book1.borrow_item()
except Exception as e:
    print(e)

print()

# #####################################################################################################################

# Task 5: Handle Return Exceptions
'''
Scenario: Celina sometimes faces issues when someone tries to return a journal that hasn’t been borrowed yet. 
This creates an opportunity to ensure such mistakes are handled gracefully.
Task: Simulate and handle the exception when trying to return a journal that has not been borrowed.
Details:
1. Process:
    - Use the Journal object from Task 3.
    - Attempt to return the journal without it being borrowed first.
2. Exception Handling:
    - Catch the exception that occurs when trying to return the un-borrowed journal.
    - Print the exception message.
This will assist Celina in managing return processes more efficiently and prevent unnecessary errors.
'''

try:
    book4.return_item()
except Exception as e:
    print(e)