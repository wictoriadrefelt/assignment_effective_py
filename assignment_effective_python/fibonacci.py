

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input('Enter a number: '))
f_sequence = [fibonacci(i) for i in range(0, n)]
print(f_sequence)

