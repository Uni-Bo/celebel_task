def lower_triangular(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j < i:
                print(" ", end="")
            else:
                print("*", end="")
        print()

def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Example usage
n = 5
print("Lower Triangular Pattern:")
lower_triangular(n)
print("\nUpper Triangular Pattern:")
upper_triangular(n)
print("\nPyramid Pattern:")
pyramid(n)
