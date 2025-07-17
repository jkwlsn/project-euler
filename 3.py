"""Problem 3: Largest Prime Factors

The prime factors of **13195** are **5, 7, 13** and **29**.

What is the largest prime factor of the number **600851475143**?
"""


def largest_prime_factors(number: int) -> list[int]:
    largest_prime: int = -1

    while number % 2 == 0:
        largest_prime = 2
        number //= 2

    i = 3
    while i * i <= number:
        while number % i == 0:
            largest_prime = i
            number //= i
        i += 2

    if number > 2:
        largest_prime = number

    print(largest_prime)
    return largest_prime


if __name__ == "__main__":
    largest_prime_factors(100)
    largest_prime_factors(13195)
    largest_prime_factors(600851475143)
