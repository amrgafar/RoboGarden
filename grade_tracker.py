import os

def add_grade():
    try:
        subject = input("Enter the subject: ")
        grade = float(input("Enter the grade: "))
        with open("grades.txt", "a") as file:
            file.write(f"{subject},{grade}\n")
            print("Grade added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid grade.")
    except IOError:
        print("An error occurred while writing to the file.")

def view_grades():
    try:
        if not os.path.exists("grades.txt"):
            raise FileNotFoundError("No grades found.")
        with open("grades.txt", "r") as file:
            grades = file.readlines()
            if not grades:
                print("No grades found.")
            else:
                print("Your grades:")
                for grade in grades:
                    subject, score = grade.strip().split(',')
                    print(f"Subject: {subject}, Grade: {score}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IOError:
        print("An error occurred while reading the file.")

def calculate_average():
    try:
        if not os.path.exists("grades.txt"):
            raise FileNotFoundError("No grades found.")
        with open("grades.txt", "r") as file:
            grades = file.readlines()
            if not grades:
                print("No grades found.")
            else:
                total = 0
                count = 0
                for grade in grades:
                    _, score = grade.strip().split(',')
                    total += float(score)
                    count += 1
                average = total / count
                print(f"Your average grade is: {average:.2f}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IOError:
        print("An error occurred while reading the file.")
    except ValueError:
        print("An error occurred while calculating the average grade.")

def main():
    while True:
        print("\nGrade Tracking Application")
        print("1. Add a new grade")
        print("2. View all grades")
        print("3. Calculate average grade")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_grade()
        elif choice == "2":
            view_grades()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
