"""Project Euler Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


def natural_numbers_below(max) -> list:
    nat_nums = [n for n in range(max) if n > 0 and n % 3 == 0 or n > 0 and n % 5 == 0]
    print(f"Natural numbers below {max}:\t{nat_nums}")
    print(f"Sum of natural numbers below {max}:\t{sum(nat_nums)}")
    return sum(nat_nums)


if __name__ == "__main__":
    natural_numbers_below(10)
    natural_numbers_below(1000)
