# Binary Search Algorithm, going through the List

"""
With a sorted data-set, we can take advantage of the ordering to make a sort which is more efficient than going element by element.

Binary search requires a sorted data-set. We then take the following steps:

Check the middle value of the dataset.

If this value matches our target we can return the index.
If the middle value is less than our target

Start at step 1 using the right half of the list.
If the middle value is greater than our target

Start at step 1 using the left half of the list.

In each iteration, we are cutting the list in half. The time complexity is O(log N).

In the worst case of 64 Elements:

Comparison 1: We look at the middle of all 64 elements

Comparison 2: If the middle is not equal to our search value, we would look at 32 elements

Comparison 3: If the new middle is not equal to our search value, we would look at 16 elements

Comparison 4: If the new middle is not equal to our search value, we would look at 8 elements

Comparison 5: If the new middle is not equal to our search value, we would look at 4 elements

Comparison 6: If the new middle is not equal to our search value, we would look at 2 elements

A sorted data-set speeds up searching by a significant amount!

"""

import time

# starting time
start = time.time()

#Iteration method:
def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  # fill in the condition for the while loop
  while left_pointer < right_pointer:
    # calculate the middle index using the two pointers
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      # set the right_pointer to the appropriate value
      right_pointer = mid_idx
    if target > mid_val:
      # set the left_pointer to the appropriate value
      left_pointer = mid_idx + 1
  
  return "Value not in list"

# sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

# End time
end = time.time()

# test cases
print(binary_search([5,6,7,8,9], 9))

# total time taken
print(f"Runtime of the iterative function is {end - start}")


# starting time
start = time.time()

#Recursion method:
def binary_search_r(sorted_list, target, low, high):
    if low > high:
        return -1;
    mid_idx = (low + high) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      # return the function again making a recursive call
      return binary_search_r(sorted_list, target, low, mid_idx-1)
    if target > mid_val:
      # set the left_pointer to the appropriate value
      return binary_search_r(sorted_list, target, mid_idx+1,high)
  
    return "Value not in list"
  

# sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

# End time
end = time.time()

# test cases
values = [5,6,7,8,9]
start_of_values = 0
end_of_values = len(values)
print(binary_search_r(values, 9, start_of_values,end_of_values))

# total time taken
print(f"Runtime of the recursive function is {end - start}")