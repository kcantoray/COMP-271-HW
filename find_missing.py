
# COMP 271
# Assignment 7 - Exercise 2


# Pseudocode:
# Start with the missing number set to min_val.
# Go through every number from min_val to max_val.
# For each number, search through the entire list.
# If the number is found, mark it as found.
# If the number is not found, save it as the missing number.
# Return the missing number.


def find_missing_linear(
    numbers: list[int],
    min_val: int,
    max_val: int
) -> int:
    """Find the missing number by using a linear search."""
    missing_number = min_val

    for candidate in range(min_val, max_val + 1):
        found = False

        for index in range(len(numbers)):
            if numbers[index] == candidate:
                found = True

        if not found:
            missing_number = candidate

    return missing_number


# Pseudocode:
# Sort the list using the sort method.
# Start the binary search with the first and last indexes.
# Find the middle index.
# Calculate the value that should be at that index.
# If the actual value matches, search the right half.
# Otherwise, search the left half.
# When the search ends, calculate and return the missing number.


def find_missing_binary_helper(
    numbers: list[int],
    min_val: int,
    left: int,
    right: int
) -> int:
    """Recursively find the first index where the expected value is missing."""
    if left > right:
        missing_number = min_val + left
    else:
        middle = (left + right) // 2
        expected_value = min_val + middle

        if numbers[middle] == expected_value:
            missing_number = find_missing_binary_helper(
                numbers, min_val, middle + 1, right
            )
        else:
            missing_number = find_missing_binary_helper(
                numbers, min_val, left, middle - 1
            )

    return missing_number


# Pseudocode:
# Sort the list using the sort method.
# Call the recursive helper with the first and last indexes.
# Return the missing number found by the helper.


def find_missing_binary_rec(
    numbers: list[int],
    min_val: int,
    max_val: int
) -> int:
    """Find the missing number using recursive binary search."""
    numbers.sort()

    missing_number = find_missing_binary_helper(
        numbers, min_val, 0, len(numbers) - 1
    )

    return missing_number


# Pseudocode:
# Sort the list using the sort method.
# Set the left and right indexes.
# Use binary search to find the first index that does not match
# the expected value based on the first number in the list.
# If the values match, search the right half.
# Otherwise, search the left half.
# Calculate and return the missing number.


def find_missing_binary_iter(numbers: list[int]) -> int:
    """Find an internal or ending missing number using iterative binary search."""
    numbers.sort()

    left = 0
    right = len(numbers) - 1
    min_val = numbers[0]

    while left <= right:
        middle = (left + right) // 2
        expected_value = min_val + middle

        if numbers[middle] == expected_value:
            left = middle + 1
        else:
            right = middle - 1

    missing_number = min_val + left

    return missing_number


numbers = [5, 2, 8, 1, 6, 3, 7]

print(find_missing_linear(numbers, 1, 8))

numbers = [5, 2, 8, 1, 6, 3, 7]

print(find_missing_binary_rec(numbers, 1, 8))

numbers = [5, 2, 8, 1, 6, 3, 7]

print(find_missing_binary_iter(numbers))
