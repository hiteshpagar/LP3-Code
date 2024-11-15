def fibonacci_recursive(n):
    """
    Recursive implementation of Fibonacci.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_non_recursive(n):
    """
    Non-recursive (iterative) implementation of Fibonacci.
    """
    if n <= 1:
        return n

    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update to the next Fibonacci number
    return b


def main():
    """
    Main function to get user input and calculate Fibonacci using both methods.
    """
    n = int(input("Enter the value of n: "))

    # Calculate using both methods
    recursive_result = fibonacci_recursive(n)
    non_recursive_result = fibonacci_non_recursive(n)

    # Print results
    print(f"Fibonacci (Recursive) of {n} is: {recursive_result}")
    print(f"Fibonacci (Non-Recursive) of {n} is: {non_recursive_result}")


if __name__ == "__main__":
    main()
