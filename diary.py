import os

def write_entry():
    try:
        with open("diary.txt", "a") as file:
            entry = input("Write your diary entry: ")
            file.write(entry + "\n")
            print("Entry saved successfully.")
    except IOError:
        print("An error occurred while writing to the file.")

def view_entries():
    try:
        if not os.path.exists("diary.txt"):
            raise FileNotFoundError("No diary entries found.")
        with open("diary.txt", "r") as file:
            entries = file.readlines()
            if not entries:
                print("No diary entries found.")
            else:
                print("Your diary entries:")
                for entry in entries:
                    print(entry.strip())
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IOError:
        print("An error occurred while reading the file.")

def main():
    while True:
        print("\nPersonal Diary Application")
        print("1. Write a new entry")
        print("2. View previous entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
