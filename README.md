# 🧪 Python Testing using Pytest

> A structured, beginner-to-intermediate assignment covering the core features of **pytest** through 9 progressive tasks — from your first `assert` all the way to writing tests before the code (TDD).

<br>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-9.x-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Tests](https://img.shields.io/badge/38%20Tests-Passing-2ECC71?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

---

## 📂 Repository Structure

```
Python-Testing-using-Pytest/
│
├── source_code.py       # All source functions & classes (Tasks 1–9)
├── test_all_tasks.py    # All 38 tests — imports from source_code.py
└── README.md
```

> **Design choice:** source code and tests live in two separate files.  
> `source_code.py` is what gets tested. `test_all_tasks.py` contains every test case.  
> Place both in the same folder and run `pytest`.

---

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/shaheershaikh943/Python-Testing-using-Pytest.git
cd Python-Testing-using-Pytest

# 2. Install pytest
pip install pytest

# 3. Run all 38 tests
pytest -v test_all_tasks.py
```

---

## 📋 What's Inside `source_code.py`

All functions and classes used across every task — fully documented with docstrings.

| Function / Class | Task | Description |
|---|---|---|
| `square(n)` | 1 | Returns `n * n` |
| `is_even(n)` | 2 | Returns `True` if n is even *(bug fixed: was `== 1`)* |
| `celsius_to_fahrenheit(c)` | 5 | Converts °C → °F |
| `average(numbers)` | 5 | Returns arithmetic mean of a list |
| `is_leap_year(year)` | 6 | Leap year check using the 4/100/400 rule |
| `reverse_string(text)` | 3 | Reverses string with `[::-1]` |
| `count_vowels(text)` | 3 | Counts vowels, case-insensitive |
| `find_max(numbers)` | 4 | Finds max; raises `ValueError` on empty list |
| `ShoppingCart` | 7 | Class with `add_item()`, `total()`, `count()` |
| `count_lines(path)` | 8 | Returns number of lines in a file |
| `fizzbuzz(n)` | 9 | Returns `"Fizz"` / `"Buzz"` / `"FizzBuzz"` / `str(n)` |

---

## 🗂️ Tasks Overview

| # | Task | Difficulty | Pytest Concept |
|---|---|---|---|
| 1 | Your Very First Test | 🟢 Easy | Plain `assert` |
| 2 | Find the Bug | 🟢 Easy | Tests reveal bugs — fix code, not tests |
| 3 | Testing String Functions | 🟢 Easy | Multiple functions + edge cases |
| 4 | Testing Errors | 🟢 Easy | `pytest.raises` + `match=` |
| 5 | Comparing Decimals | 🟡 Medium | `pytest.approx` |
| 6 | Many Inputs | 🟡 Medium | `@pytest.mark.parametrize` |
| 7 | Reusing Setup | 🟡 Medium | `@pytest.fixture` |
| 8 | Testing Files | 🟡 Medium | `tmp_path` built-in fixture |
| 9 | FizzBuzz TDD | 🔴 Challenge | Write tests before the code |

---

## 🔍 Task Breakdown

<details>
<summary><b>Task 1 🟢 — Your Very First Test</b></summary>

Testing `square(n)` with plain `assert` statements.

```python
def test_square_positive():
    assert square(4) == 16        # 4 × 4 = 16

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-3) == 9        # negative × negative = positive
```
</details>

<details>
<summary><b>Task 2 🟢 — Find the Bug</b></summary>

The original `is_even()` had a bug — it used `== 1` instead of `== 0`, making it return `True` for **odd** numbers. Tests are written first; they fail. Then the source is fixed until they pass.

```python
# BUG (original):   return n % 2 == 1
# FIX (corrected):  return n % 2 == 0

def test_is_even_with_even_number():
    assert is_even(4) == True

def test_is_even_with_odd_number():
    assert is_even(7) == False
```

> ⚠️ **Rule:** Never change a test to make it pass. Fix the source code.
</details>

<details>
<summary><b>Task 3 🟢 — Testing String Functions</b></summary>

Testing `reverse_string()` and `count_vowels()` including edge cases like empty strings and uppercase input.

```python
def test_reverse_empty_string():
    assert reverse_string("") == ""

def test_count_vowels_uppercase():
    assert count_vowels("HELLO") == 2    # case-insensitive: E, O

def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0
```
</details>

<details>
<summary><b>Task 4 🟢 — Testing Errors with <code>pytest.raises</code></b></summary>

Verifying that `find_max([])` raises a `ValueError` with the correct message.

```python
def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        find_max([])

# Bonus: check the error message text
def test_empty_list_error_message():
    with pytest.raises(ValueError, match="List is empty"):
        find_max([])
```

> 💡 If **no** exception is raised inside the `with` block, the test **fails**.
</details>

<details>
<summary><b>Task 5 🟡 — Comparing Decimals with <code>pytest.approx</code></b></summary>

Floating-point arithmetic is imprecise inside computers: `0.1 + 0.2 + 0.3 ≠ 0.6` exactly. `pytest.approx` adds a tolerance.

```python
def test_average_with_approx():
    # Without approx this would FAIL due to floating-point precision
    assert average([0.1, 0.2, 0.3]) == pytest.approx(0.2)

def test_body_temperature():
    assert celsius_to_fahrenheit(37.5) == pytest.approx(99.5)
```
</details>

<details>
<summary><b>Task 6 🟡 — Many Inputs with <code>@pytest.mark.parametrize</code></b></summary>

One test function that runs once per `(year, expected)` pair — each appears as a separate line in `pytest -v`.

```python
@pytest.mark.parametrize("year, expected", [
    (2024, True),    # divisible by 4, not 100      → leap year
    (1900, False),   # divisible by 100, not 400    → NOT a leap year
    (2000, True),    # divisible by 400             → leap year
    (2023, False),   # not divisible by 4           → NOT a leap year
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected
```
</details>

<details>
<summary><b>Task 7 🟡 — Reusing Setup with <code>@pytest.fixture</code></b></summary>

A fixture pre-loads a `ShoppingCart` so every test starts with fresh, consistent state.

```python
@pytest.fixture
def cart():
    c = ShoppingCart()
    c.add_item("pen",      price=50,  qty=2)   # subtotal: 100
    c.add_item("notebook", price=200, qty=1)   # subtotal: 200
    return c                                   # total: 300, count: 3

def test_cart_total(cart):       # pytest injects 'cart' automatically
    assert cart.total() == 300

def test_negative_price_raises():
    c = ShoppingCart()
    with pytest.raises(ValueError):
        c.add_item("item", price=-10)
```
</details>

<details>
<summary><b>Task 8 🟡 — Testing Files with <code>tmp_path</code></b></summary>

`tmp_path` is a built-in pytest fixture that gives each test a unique temporary directory, auto-deleted after the run — no real files left behind.

```python
def test_count_three_lines(tmp_path):
    f = tmp_path / "notes.txt"
    f.write_text("line one\nline two\nline three\n")
    assert count_lines(f) == 3

def test_count_empty_file(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")
    assert count_lines(f) == 0
```
</details>

<details>
<summary><b>Task 9 🔴 — FizzBuzz TDD Challenge</b></summary>

Tests are written **before** the implementation. The tests fail first, then `fizzbuzz()` is written in `source_code.py` until all pass.

```python
@pytest.mark.parametrize("n, expected", [
    (3,  "Fizz"),
    (5,  "Buzz"),
    (15, "FizzBuzz"),   # check % 15 FIRST or this wrongly returns "Fizz"
    (7,  "7"),
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
```

> 🔴 **TDD Flow:** Write tests → Watch them fail → Write the code → Watch them pass.
</details>

---

## ▶️ Running Tests

```bash
# Run all tests (verbose)
pytest -v test_all_tasks.py

# Run a single test function
pytest -v test_all_tasks.py::test_cart_total

# Run tests matching a keyword
pytest -v -k "leap_year"

# Run and show print output
pytest -v -s test_all_tasks.py

# Stop after first failure
pytest -x test_all_tasks.py
```

### Expected Output

```
test_all_tasks.py::test_square_positive              PASSED  [  2%]
test_all_tasks.py::test_square_zero                  PASSED  [  5%]
test_all_tasks.py::test_square_negative              PASSED  [  7%]
test_all_tasks.py::test_is_even_with_even_number     PASSED  [ 10%]
...
test_all_tasks.py::test_fizzbuzz[15-FizzBuzz]        PASSED  [ 94%]
test_all_tasks.py::test_fizzbuzz[30-FizzBuzz]        PASSED  [ 97%]
test_all_tasks.py::test_fizzbuzz[7-7]                PASSED  [100%]

========== 38 passed in 0.16s ==========
```

---

## 📌 Key Rules & Gotchas

| Rule | Why it matters |
|---|---|
| Every test function name must start with `test_` | pytest won't discover it otherwise |
| Fix bugs in **source code**, never in tests | Tests describe correct behaviour |
| Use `pytest.approx` for float comparisons | `0.1 + 0.2 + 0.3 ≠ 0.6` exactly |
| Check `% 15` **before** `% 3` or `% 5` in FizzBuzz | Order of conditions changes the result |
| `tmp_path` for file tests — never write to the real project folder | Keeps the repo clean |
| `@pytest.fixture` is injected by **parameter name**, not import | Name the param to match the fixture |

---

## 🛠️ Requirements

| Dependency | Version |
|---|---|
| Python | 3.8 + |
| pytest | 7.x or 9.x |

Install with:

```bash
pip install pytest
```

No other dependencies required.

---

## 👤 Author

**Shaheer** — [@shaheershaikh943](https://github.com/shaheershaikh943)

Educational tech content creator · **Vickybytes** on YouTube  
Building coding projects, tutorials, and beginner-friendly Python content.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ for learners exploring Python testing
</p>
