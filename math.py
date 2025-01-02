def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = [1, 2, 3, 4, 5]  # Example list of numbers
    average = calculate_average(numbers)
    print("The average of the list is:", average)
    return average

main()
