def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    # Prompt the user for the value of N
    N = int(input("Enter a number (N): "))

    # Print all prime numbers between 2 and N
    print(f"Prime numbers between 2 and {N}:")
    for num in range(2, N + 1):
        if is_prime(num):
            print(num, end=" ")

if __name__ == "__main__":
    main()
