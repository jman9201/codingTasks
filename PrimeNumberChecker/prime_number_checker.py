def is_prime(n):
    """
    Check if a number is prime.
    A prime number is only divisible by 1 and itself.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):
        # Check from 2 to the square root of n
        if n % i == 0:
            # If n is divisible by any number in this range, it is not prime
            return False
    return True  # If no divisors were found, n is prime


if __name__ == "__main__":
    # Ask the user for input
    number = int(input("Enter a number to check if it is prime: "))

    # Check if the number is prime and display the result
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
