"""Worker functions for the notebook concurrency_parallelism.ipynb.

Processes started with the `spawn` method (the default on macOS and Windows)
import the functions they run. A function defined in a notebook cell cannot be
imported, but one defined in a module like this one can.
"""


def count_primes(n):
    """Return the number of primes below n (pure Python, CPU-bound on purpose)."""
    count = 0
    for k in range(2, n):
        for d in range(2, int(k ** 0.5) + 1):
            if k % d == 0:
                break
        else:
            count += 1
    return count


def fibonacci(n):
    """Return the n-th Fibonacci number, by slow recursion (CPU-bound on purpose)."""
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
