import random
from arr_math import sum_array, mult_array
#from arr_sort import bubble_sort

random_array = [random.randint(0, 10) for _ in range(5)]

total_sum = sum_array(random_array)
total_mult = mult_array(random_array)
#arr_sort = bubble_sort(random_array)

print(f"Generated Array:\n {random_array}\n")
print(f"Sum: {total_sum}\n")
print(f"Mult: {total_mult}\n")
#print(f"Sorted:\n {arr_sort}\n")