import math


def generate_prime_numbers(x):
    primes = set()
    count = 0
    n = 2
    while count < x:
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n
            count = count + 1
        n = n + 1


def gen_fibonacci(y):
    c, n = 0, 1
    for i in range(y):
        c, n = n, c + n
        yield c


def square(number_list):
    for i in number_list:
        i = i**2
        yield i


def square_root(number_list):
    for i in number_list:
        i = math.sqrt(i)
        yield i


quantity_of_number = int(input("How many number count? "))

generated_prime = list(generate_prime_numbers(quantity_of_number))
generated_fibonacci = list(gen_fibonacci(quantity_of_number))

square_prime = list(square(generated_prime))
square_fibonacci = list(square(generated_fibonacci))

square_list = list(tuple(map(sum, zip(square_prime, square_fibonacci))))
print(f"List of sum of squares for Fibonacci sequence and prime numbers: \n{square_list}")

results = list(square_root(square_list))
print(f"List of roots of sums of squares for Fibonacci sequence and prime numbers: \n{results}")
