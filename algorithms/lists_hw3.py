lst_words = ['apple', 'kiwi', 'banana', 'orange']
lst_num = [3,4,2,1]

# print(lst_words[-1])


def find_miss_element(arr1, arr2):
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)
    for i in range(len(arr2) -1):
        if arr1[i] != arr2[i]:
            print(str(arr1[i]) + " is the missing element")
            return
    print(str(arr1[-1]) + ' is the missing element')

test1 = [1, 2, 3, 4, 5, 6]
test2 = [3, 2, 6, 5, 1]
find_miss_element(test1, test2)

def largest_cont_sum(arr: list):
    cur_sum = max_sum = arr[0]
    for num in arr[1:]:
        cur_sum = max(cur_sum +num, num)
        max_sum = max(max_sum, cur_sum)

    return max_sum
test_list = [-4, 2, -1, 3, 4, 10, 10, -1, -1]
print(largest_cont_sum(test_list))

#Mountain Array
def is_mountain_array(arr):
    i = 1
    while i < len(arr) and arr[i-1] < arr[i]:
        i =+ 1
    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i - 1] > arr[i]:
        i += 1
    if i == len(arr):
        return True
    else:
        return False


array = [1, 3, 4, 7, 5, 3]
print(is_mountain_array(array))





