# Define the Student class
class Student:
    def __init__(self, name, age, grades):
        self.name = name  # Student's name
        self.age = age    # Student's age
        self.grades = grades  # List of student's grades

    def display_info(self):
        """Displays the student's name, age, and grades."""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
    
    def average_grade(self):
        """Calculates and returns the average grade of the student."""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def add_grade(self, grade):
        """Adds a new grade to the student's record."""
        self.grades.append(grade)

# Define a class to manage the student database
class StudentDatabase:
    def __init__(self):
        self.students = []  # List to store student objects

    def add_student(self, student):
        """Adds a student to the database."""
        self.students.append(student)

    def display_all_students(self):
        """Displays information for all students in the database."""
        for student in self.students:
            student.display_info()
            print(f"Average Grade: {student.average_grade()}\n")

# Main function to simulate student database operations
def main():
    # Create an instance of StudentDatabase
    db = StudentDatabase()

    # Create some student objects
    student1 = Student("John Doe", 20, [88, 92, 85])
    student2 = Student("Alice Smith", 22, [79, 85, 90, 93])
    student3 = Student("Bob Johnson", 19, [90, 88, 84, 87])

    # Add students to the database
    db.add_student(student1)
    db.add_student(student2)
    db.add_student(student3)

    # Display all students and their information
    db.display_all_students()

    # Add a new grade for a student
    student1.add_grade(95)
    print("\nAfter adding a new grade for John Doe:\n")
    db.display_all_students()

# Run the main function
if __name__ == "__main__":
    main()
