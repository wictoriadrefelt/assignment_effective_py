import time


def int_to_string(n):
    value = f'{n}'
    return value


def convert(i):
    number = str(i)
    return number


def main():
    first = int_to_string(34)
    print(type(first))

    second = convert(34)
    print(type(second))


if __name__ == '__main__':
    main()
