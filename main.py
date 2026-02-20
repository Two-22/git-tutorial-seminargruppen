import random
from arr_math import sum_array
#from arr_sort import bubble_sort

random_array = [random.randint(0, 10) for _ in range(5)]

total = sum_array(random_array)
#arr_sort = bubble_sort(random_array)

print(f"Generated Array:\n {random_array}\n")
print(f"Produkt: {total}\n")
#print(f"Sorted:\n {arr_sort}\n")