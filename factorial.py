def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = 5  # Example number
    result = factorial(number)
    print("The factorial of", number, "is:", result)
    return result

main()
