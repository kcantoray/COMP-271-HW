
# COMP 271
# Assignment 7 - Exercise 1


# Pseudocode:
# Set the ending position to the last index.
# Continue while the list is not sorted and there are elements to compare.
# Set swapped to False at the beginning of each pass.
# Compare adjacent elements, starting from the end.
# If the left element is larger, swap the two elements.
# If a swap happens, set swapped to True.
# Print the list after each pass.
# Move the ending position one step toward the beginning.


def bubble_sort(numbers: list[int]) -> None:
    """Sort the list by moving the smallest remaining value to the beginning."""
    end = len(numbers) - 1
    swapped = True

    while swapped and end > 0:
        swapped = False

        for index in range(end, 0, -1):
            if numbers[index] < numbers[index - 1]:
                temp = numbers[index]
                numbers[index] = numbers[index - 1]
                numbers[index - 1] = temp
                swapped = True

        print(numbers)
        end -= 1


# Q2:
# Best-case time complexity: O(n).
# This happens when the list is already sorted because the algorithm
# only needs one pass to check the list and makes no swaps.
#
# Worst-case time complexity: O(n^2).
# This happens when the list is in reverse order because the algorithm
# needs multiple passes to move all the smaller values to the beginning.

