"""Problem 4: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two **2**-digit numbers is **9009 =  91 \* 99**.

Find the largest palindrome made from the product of two **3**-digit numbers."""


def largest_palindrome_product() -> int:
    max_ = range(999, 99, -1)
    max_palindrome = 0
    factors = ()
    for x in max_:
        for y in max_:
            product = x * y
            if product >= max_palindrome:
                if str(product) == str(product)[::-1]:
                    max_palindrome = product
                    factors = (x, y)
    print(max_palindrome, factors)
    return max_palindrome


if __name__ == "__main__":
    largest_palindrome_product()
