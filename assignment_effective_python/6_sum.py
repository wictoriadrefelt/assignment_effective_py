

def add_total(n):
    total = sum(n)
    return total


def func(n):
    split_nums = [int(i) for i in str(n)]
    return add_total(split_nums)


def main():
    print(func(45))
    print(func(124))


if __name__ == '__main__':
    main()
