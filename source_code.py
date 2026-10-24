"""
=============================================================================
  SOURCE CODE — All Functions & Classes
  Contains: mymath, text_tools, list_tools, cart, file_tools, fizzbuzz
=============================================================================
"""


# =============================================================================
# mymath  —  Tasks 1, 2, 5, 6
# =============================================================================

def square(n):
    """Return n squared."""
    return n * n


def is_even(n):
    """Return True if n is even. (Bug fix: original was == 1, corrected to == 0)"""
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def is_leap_year(year):
    """
    Return True if year is a leap year.
    Rule: divisible by 4 AND (not by 100 OR by 400).
    """
    return year % 4 == 0 and (
        year % 100 != 0 or year % 400 == 0
    )


# =============================================================================
# text_tools  —  Task 3
# =============================================================================

def reverse_string(text):
    """Return text reversed using Python slice notation."""
    return text[::-1]


def count_vowels(text):
    """Return the number of vowels (a e i o u) in text, case-insensitive."""
    return sum(1 for ch in text.lower() if ch in "aeiou")


# =============================================================================
# list_tools  —  Task 4
# =============================================================================

def find_max(numbers):
    """
    Return the largest number in a list.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


# =============================================================================
# cart  —  Task 7
# =============================================================================

class ShoppingCart:
    """A simple shopping cart that stores items with price and quantity."""

    def __init__(self):
        self.items = {}                        # { name: (price, qty) }

    def add_item(self, name, price, qty=1):
        """Add an item to the cart. Raises ValueError for invalid inputs."""
        if price < 0 or qty < 1:
            raise ValueError("Invalid price or quantity")
        self.items[name] = (price, qty)

    def total(self):
        """Return the total cost of all items (price × quantity)."""
        return sum(p * q for p, q in self.items.values())

    def count(self):
        """Return the total number of individual items in the cart."""
        return sum(q for _, q in self.items.values())


# =============================================================================
# file_tools  —  Task 8
# =============================================================================

def count_lines(path):
    """Return the number of lines in the file at the given path."""
    with open(path) as f:
        return len(f.readlines())


# =============================================================================
# fizzbuzz  —  Task 9 (TDD Challenge)
# =============================================================================

def fizzbuzz(n):
    """
    Return 'FizzBuzz' if n divisible by 15,
           'Fizz'     if n divisible by 3,
           'Buzz'     if n divisible by 5,
           str(n)     otherwise.
    NOTE: check % 15 FIRST to correctly catch numbers divisible by both.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
