# Linear Search Algorithm, going through the List
"""
The linear search, or sequential search, algorithm sequentially checks whether a given value is an element of a specified list 
by scanning the elements of a list one-by-one. It checks every item in the list in order from the beginning to end until it finds a target value.
If it finds the target value in the list, the linear search algorithm stops and returns the position in the list corresponding to the target value. 
If it does not find the value, the linear search algorithm returns a message stating that the target value is not in the list.

The steps are:
1. Examine the first element of the list.
2. If the first element is equal to the target value, stop.
3. If the first element is not equal to the target value, check the next element in the list.
4. Continue steps 1-3 until the element is found or the end of the list is reached.

Best Case Performance
The best case performance for linear search occurs when the target value exists in the list and is in the first position of the list.
The time complexity for linear search in its best case is O(1)

Worst Case Performance
Case 1: when the target value at the end of the list.
Case 2: when the target value does not exist in the list.
For this reason, the time complexity for linear search in its worst case is O(N).

Average Case Performance
On average it would be in the middle of the list, that search would take O(N/2) time

Time Complexity of Linear Search
Linear search runs in linear time. Its efficiency can be expressed as a linear function, with the number of comparisons to find a target increasing 
linearly as the size of the list, N, increases.

The time complexity for linear search in Big-O notation is O(N).

A time complexity of O(N) means the number of comparisons is proportional to the number of elements, N, in the list. With a list with twice 
as many elements, linear search will take at most twice as long to perform the search. The time complexity of linear search is also dependent 
on the best case, worst case, and average case scenarios.

Linear search is a good choice for a search algorithm when:

You expect the target value to be positioned near the beginning of the list.

A search needs to be performed on an unsorted list because linear search traverses the entire list from beginning to end, regardless of its order.
"""

# A list of the ingredients for tuna sushi

import time


recipe = ["nori", "tuna", "soy sauce", "sushi rice", "sushi rice", "sushi rice", "sushi rice", "sushi rice", "sushi rice", "sushi rice","test22"]
target_ingredient = "test22"
# starting time
start = time.time()
def linear_search(search_list, target_value):

  
  #Running Linear Search on an unsorted List
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

# sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

# End time
end = time.time()

# Printing out the number
print(linear_search(recipe, target_ingredient))

# total time taken
print(f"Runtime of the function is {end - start}")

