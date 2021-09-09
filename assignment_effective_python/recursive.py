
def recursion_sum(my_list):
   my_total = 0
   for elem in my_list:
      if (type(elem) == type([])):
         my_total = my_total + recursion_sum(elem)
      else:
         my_total = my_total + elem
   return my_total

my_list = [1, 2, [3,4], [5,6]]
print(recursion_sum(my_list))