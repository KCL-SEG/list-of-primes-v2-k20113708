"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    prime = 2

    if number_of_primes <= 0:
        raise ValueError

    while len(list) < number_of_primes:
        list.append(prime)
        num = prime + 1
        while not isPrime(num):
            num += 1
        prime = num

    return list


def isPrime(number):
    counter = 2
    while counter < number:
        if number % counter == 0:
            return False
        counter += 1
    return True
