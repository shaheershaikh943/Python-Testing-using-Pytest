"""
=============================================================================
  TEST FILE — All Tasks (1 through 9)
  Imports everything from source_code.py
  Run: pytest -v test_all_tasks.py
=============================================================================
"""

import pytest
from source_code import (
    # mymath
    square,
    is_even,
    celsius_to_fahrenheit,
    average,
    is_leap_year,
    # text_tools
    reverse_string,
    count_vowels,
    # list_tools
    find_max,
    # cart
    ShoppingCart,
    # file_tools
    count_lines,
    # fizzbuzz
    fizzbuzz,
)


# =============================================================================
# TASK 1 · EASY — Your Very First Test
# Concept: plain assert statements
# =============================================================================

def test_square_positive():
    assert square(4) == 16              # 4 × 4 = 16

def test_square_zero():
    assert square(0) == 0               # 0 × 0 = 0

def test_square_negative():
    assert square(-3) == 9             # -3 × -3 = 9 (negatives cancel out)


# =============================================================================
# TASK 2 · EASY — Find the Bug
# Concept: tests reveal bugs; fix the code, not the tests
# Original bug: (n % 2 == 1) → True for odd numbers, not even ones
# Fix applied in source_code.py: changed == 1  to  == 0
# =============================================================================

def test_is_even_with_even_number():
    assert is_even(4) == True          # 4 is even → must return True

def test_is_even_with_odd_number():
    assert is_even(7) == False         # 7 is odd  → must return False


# =============================================================================
# TASK 3 · EASY — Testing String Functions
# Concept: test multiple functions with edge cases (empty string, uppercase)
# =============================================================================

# --- reverse_string ---

def test_reverse_normal_word():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    assert reverse_string("") == ""    # edge case: empty input → empty output

# --- count_vowels ---

def test_count_vowels_normal_word():
    assert count_vowels("Pakistan") == 3   # vowels: a, i, a

def test_count_vowels_uppercase():
    assert count_vowels("HELLO") == 2      # case-insensitive: counts E and O

def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0    # no vowels at all


# =============================================================================
# TASK 4 · EASY — Testing Errors with pytest.raises
# Concept: verify a function raises the correct exception type and message
# =============================================================================

def test_find_max_positive_numbers():
    assert find_max([3, 1, 4, 1, 5, 9]) == 9

def test_find_max_negative_numbers():
    assert find_max([-10, -3, -7]) == -3   # -3 is the largest among negatives

def test_find_max_single_item():
    assert find_max([42]) == 42

def test_empty_list_raises_value_error():
    # If no ValueError is raised inside the block, this test FAILS
    with pytest.raises(ValueError):
        find_max([])

def test_empty_list_error_message():
    # Bonus: match= checks the error message text using a regex substring
    with pytest.raises(ValueError, match="List is empty"):
        find_max([])


# =============================================================================
# TASK 5 · MEDIUM — Comparing Decimals with pytest.approx
# Concept: floating-point numbers are not exactly equal; approx adds tolerance
# Example: 0.1 + 0.2 + 0.3 is 0.6000000000000001 inside a computer
# =============================================================================

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212       # exact integer result, no approx needed

def test_body_temperature():
    # 37.5°C = 99.5°F — use approx because of float arithmetic
    assert celsius_to_fahrenheit(37.5) == pytest.approx(99.5)

def test_average_with_approx():
    # Without approx this would FAIL due to floating-point precision error
    assert average([0.1, 0.2, 0.3]) == pytest.approx(0.2)


# =============================================================================
# TASK 6 · MEDIUM — Many Inputs with @pytest.mark.parametrize
# Concept: one test function runs once per (year, expected) pair
# Each pair appears as a separate line in pytest -v output
# =============================================================================

@pytest.mark.parametrize("year, expected", [
    (2024, True),   # divisible by 4, not by 100          → leap year
    (2023, False),  # not divisible by 4                  → not a leap year
    (1900, False),  # divisible by 100 but NOT by 400     → not a leap year
    (2000, True),   # divisible by 400                    → leap year
    (2100, False),  # divisible by 100, not by 400        → not a leap year
    (1600, True),   # divisible by 400                    → leap year
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected


# =============================================================================
# TASK 7 · MEDIUM — Reusing Setup with a Fixture
# Concept: @pytest.fixture runs before each test that requests it by name
# The 'cart' fixture pre-loads a ShoppingCart so every test starts fresh
# =============================================================================

@pytest.fixture
def cart():
    """
    Fixture: returns a ShoppingCart with:
        2 pens     @ price 50  → subtotal 100
        1 notebook @ price 200 → subtotal 200
        Total = 300  |  Item count = 3
    """
    c = ShoppingCart()
    c.add_item("pen",      price=50,  qty=2)
    c.add_item("notebook", price=200, qty=1)
    return c

def test_cart_total(cart):
    # pytest injects the fixture automatically because the param is named 'cart'
    assert cart.total() == 300          # 2×50 + 1×200 = 300

def test_cart_count(cart):
    assert cart.count() == 3            # 2 pens + 1 notebook = 3 items

def test_empty_cart_total():
    # This test does NOT use the fixture — starts with a brand-new empty cart
    empty = ShoppingCart()
    assert empty.total() == 0

def test_negative_price_raises():
    c = ShoppingCart()
    with pytest.raises(ValueError):
        c.add_item("broken", price=-10) # negative price must raise ValueError


# =============================================================================
# TASK 8 · MEDIUM — Testing Files with tmp_path
# Concept: tmp_path is a built-in pytest fixture that provides a unique
#          temporary directory per test; auto-deleted after the run
# =============================================================================

def test_count_three_lines(tmp_path):
    f = tmp_path / "notes.txt"
    f.write_text("line one\nline two\nline three\n")   # write 3 lines
    assert count_lines(f) == 3

def test_count_empty_file(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")                    # empty file → 0 lines
    assert count_lines(f) == 0


# =============================================================================
# TASK 9 · CHALLENGE — Write the Tests First: FizzBuzz (TDD)
# Concept: Test-Driven Development — tests written before the implementation
# Step 1 → write tests below (they fail because fizzbuzz didn't exist yet)
# Step 2 → write fizzbuzz() in source_code.py until all tests pass
# Step 3 → swap test file with a classmate and run against each other's code
# =============================================================================

@pytest.mark.parametrize("n, expected", [
    (1,  "1"),          # no rule applies → return number as string
    (3,  "Fizz"),       # divisible by 3
    (5,  "Buzz"),       # divisible by 5
    (9,  "Fizz"),       # divisible by 3, not 5
    (10, "Buzz"),       # divisible by 5, not 3
    (15, "FizzBuzz"),   # divisible by BOTH — check % 15 first or this returns "Fizz"
    (30, "FizzBuzz"),   # divisible by BOTH
    (7,  "7"),          # plain number
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
