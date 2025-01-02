# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title         # Title of the book
        self.author = author       # Author of the book
        self.available = True      # Availability status (True if available, False if checked out)

    def check_out(self):
        """Method to check out the book."""
        if self.available:
            self.available = False
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"Sorry, the book '{self.title}' is currently unavailable.")

    def return_book(self):
        """Method to return the book."""
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not checked out.")

    def display_info(self):
        """Method to display information about the book."""
        availability = "Available" if self.available else "Checked out"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {availability}")

# Define the Library class to manage the catalogue
class Library:
    def __init__(self):
        self.books = []  # List to store all books in the library

    def add_book(self, book):
        """Method to add a book to the library catalogue."""
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def display_catalogue(self):
        """Method to display the catalogue of all books in the library."""
        if not self.books:
            print("No books available in the library.")
        for book in self.books:
            book.display_info()
            print()  # Adding a space between books for readability

# Main function to demonstrate the library system
def main():
    # Create an instance of Library
    my_library = Library()

    # Create some Book objects
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Display the catalogue
    print("Library Catalogue:")
    my_library.display_catalogue()

    # Check out a book and display status
    print("\nChecking out '1984':")
    book1.check_out()

    # Try to check out the same book again
    print("\nTrying to check out '1984' again:")
    book1.check_out()

    # Return a book and display status
    print("\nReturning '1984':")
    book1.return_book()

    # Display the catalogue again after returning the book
    print("\nLibrary Catalogue after returning '1984':")
    my_library.display_catalogue()

# Run the main function
if __name__ == "__main__":
    main()
