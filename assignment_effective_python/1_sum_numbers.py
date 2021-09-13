import time
from timeit import timeit
from functools import reduce

"""
Using the built in function sum as 
is far more efficient that the other approaches tried out """


my_nums = [55, 878, 596, 601,
           170, 624, 904, 988,
           98, 529, 646, 692,
           556, 127, 794, 488]


print(sum(my_nums))

