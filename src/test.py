import time
import random
from sort_solutions import bubble_sort, selection_sort, insertion_sort, quicksort, merge_sort
​
l1 = list(range(1000))
random.shuffle(l1)
l2 = list(range(2000))
random.shuffle(l2)
l3 = list(range(3000))
random.shuffle(l3)
l4 = list(range(4000))
random.shuffle(l4)
l5 = list(range(5000))
random.shuffle(l5)
l6 = list(range(6000))
random.shuffle(l6)
l7 = list(range(7000))
random.shuffle(l7)
l8 = list(range(8000))
random.shuffle(l8)
l9 = list(range(9000))
random.shuffle(l9)
l10 = list(range(10000))
random.shuffle(l10)
​
shuffled_lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
​
​
results = []
for shuffled_list in shuffled_lists:
    l_copy = shuffled_list.copy()
    start_time = time.time()
    bubble_sort(l_copy)
    end_time = time.time()
    print(f"runtime: {end_time - start_time}")
    results.append(end_time - start_time)
​
for result in results:
    print(result)
