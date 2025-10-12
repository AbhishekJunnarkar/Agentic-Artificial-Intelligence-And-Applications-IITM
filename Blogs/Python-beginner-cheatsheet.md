# Python Data Types — Beginner Cheatsheet

## Basic Data Types

| Type | Example | Description |
|------|----------|-------------|
| **int** | `10`, `-5`, `0` | Whole numbers without a decimal point |
| **float** | `3.14`, `-2.5` | Numbers with decimals |
| **str** | `"Hello"`, `'India'` | Text or sequence of characters |
| **bool** | `True`, `False` | Logical (Boolean) values used in conditions |
| **complex** | `3+5j` | Complex numbers (real + imaginary parts) |

---

## Sequence Types

| Type | Example | Description |
|------|----------|-------------|
| **list** | `[10, 20, 30]` | Ordered, changeable (mutable) collection |
| **tuple** | `(10, 20, 30)` | Ordered, **unchangeable** (immutable) collection |
| **range** | `range(5)` | Sequence of numbers (often used in loops) |
| **str** | `"Python"` | Strings are also sequences of characters |

---

## Set Types

| Type | Example | Description |
|------|----------|-------------|
| **set** | `{1, 2, 3}` | Unordered collection with **no duplicates** |
| **frozenset** | `frozenset({1, 2, 3})` | Same as set, but **immutable** |

---

## Mapping Type

| Type | Example | Description |
|------|----------|-------------|
| **dict** | `{"name": "Aarav", "age": 13}` | Stores data in **key–value pairs** |

---

## None Type

| Type | Example | Description |
|------|----------|-------------|
| **NoneType** | `None` | Represents **no value** or **null** |

---

## Quick Examples

```python
a = 10               # int
b = 3.14             # float
c = "Hello"          # str
d = True             # bool
e = [1, 2, 3]        # list
f = (4, 5, 6)        # tuple
g = {7, 8, 9}        # set
h = {"x": 1, "y": 2} # dict
i = None             # NoneType

print(type(a), type(c), type(h))
