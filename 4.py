"""Problem 4: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two **2**-digit numbers is **9009 =  91 \* 99**.

Find the largest palindrome made from the product of two **3**-digit numbers."""

import time


def largest_palindrome_product() -> int:
    max_palindrome = 0
    factors = ()
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            product = x * y
            if product <= max_palindrome:
                break
            if str(product) == str(product)[::-1]:
                max_palindrome = product
                factors = (x, y)
    print(max_palindrome, factors)
    return max_palindrome


if __name__ == "__main__":
    start_time = time.perf_counter()
    largest_palindrome_product()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
