def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        a, b = 0, 1
        sequence = [a, b]
        while len(sequence) < n:
            next_fib = a + b
            sequence.append(next_fib)
            a = b
            b = next_fib
        return sequence

# Example usage:
print(fibonacci_iterative(10))