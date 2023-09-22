# Sorting - Nested loops and role in sorting algorithms
#selection sort, insertion sort, bubble sort
#sorting - arranging items by some criteria
#Asending order can use sort() for any list or sorted function for element
#nested loops lst= ["a", "b", "c"] aa ab ac ba bb bc
# outer loop
# for i in lst:
#  for j in lst:
#   print(i+j)
# for i in range (1,11):
#  for j in range(1,11):
adj = ["red", "ripe", "tasty"]
fruits = ["apple", "banana", "cherry"]
for i in adj:
    for j in fruits:
        print(i + j)

#selection sort
def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

test_data = [4, 2, 1, 7, 5, 3]
print(test_data)
selection_sort(test_data)
print(test_data)


# bubble sort #complexity n2
def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

test_data1 = [4,5,2,1,5]
print(test_data1)
bubble_sort(test_data1)
print(test_data1)

#insertion sort - first card is sorted and next card if higher goes to the right if less goes left
#places unsorted element to the correct location
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

test_data2 = [5,3,2,1,6,4]
print(test_data2)
insertion_sort(test_data2)
print(test_data2)
