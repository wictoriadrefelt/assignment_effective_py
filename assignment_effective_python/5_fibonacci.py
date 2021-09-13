


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    n = int(input('Enter a number: '))
    f_sequence = [fibonacci(i) for i in range(0, n)]
    print(f_sequence)


if __name__ == '__main__':
    main()
