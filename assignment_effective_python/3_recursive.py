import time

def recursion_sum(my_list):
    my_total = 0
    for num in my_list:
       if (type(num) == type([])):
          my_total = my_total + recursion_sum(num)
       else:
          my_total = my_total + num
    return my_total

def main():
    my_list = [1, 2, [3, 4], [5, 6]]
    print(recursion_sum(my_list))


if __name__ == '__main__':
    main()