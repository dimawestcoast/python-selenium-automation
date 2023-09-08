# Task 1. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.


# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
def find_two_lowest(arr: list):
    arr.sort()
    return [arr[0], arr[1]]

print(find_two_lowest([198, 3, 4, 9, 10, 9, 2]))





#Task 2
#Given a list of numbers, return the inverse of each. Each positive becomes a negative, and the negatives become positives.

# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]


def invert_list(arr: list):
    for i in range(len(arr)):
        arr[i] = -arr[i]
    return arr

print(invert_list([1, 5, -2, 4]))



# Task 3
# Implement a function that returns the difference between the largest and the smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.

# Example:
# Input: [3, 5, 7, 2]
# Output: 7 - 2 = 5


def max_diff(arr: list):
    arr.sort()
    return arr[-1] - arr[0]

print(max_diff([3, 5, 7, 2]))



# Task 4
# Write a function that counts the number of elements in a given list larger than their adjacent neighbors.

# Example:
# Input: [2, 56, 7, 21, 22, 19, 26]
# Output: 2 (56, 22)

def count_larger_neighbors(arr: list):
    count = 0

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            count += 1

    return count


print(count_larger_neighbors([2, 56, 7, 21, 22, 19, 26]))




# Task 5
# Given an array. Find the minimum element in the list and subtract it from each element in the array.

# Example:
# Input: [9, 2, 5, 4, 7, 6, 1]
# The minimum element in the list: 1
# Output: [8, 1, 4, 3, 6, 5, 0]


def subtract_min(arr: list):
    min_element = min(arr)

    for i in range(len(arr)):
        arr[i] = arr[i] - min_element

    return arr


print(subtract_min([9, 2, 5, 4, 7, 6, 1]))

