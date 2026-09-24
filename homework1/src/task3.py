def greet(name):
    # This function will print to stdout
    print(f"Hello, {name}")


def check_number(num):
    """
    Check if a number is positive, negative, or zero.
    Returns a string describing the number.
    """
    # Complete: Implement an if-elif-else statement to check:
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


def get_first_n_primes(n):
    """
    Returns a list of the first n prime numbers.
    """
    primes = []
    count = 0
    num = 2
    
    while count < n:
        # Check if num is prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
            count += 1
        
        num += 1
    
    return primes


def sum_to_n(n):
    """
    Calculate the sum of all numbers from 1 to n using a while loop.
    Returns the total sum.
    """
    total = 0
    current = 1
    while current <= n:
        total += current
        current += 1
    return total
