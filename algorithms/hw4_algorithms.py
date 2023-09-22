#1.Sum and multiplication of even and odd numbers.
#You are given an array of integers. Your task is to calculate two values:
#the sum of all even numbers and the product of all odd numbers in the array.
#Please return these two values as a list [sum_even, product_odd].

def sum_even_and_product_odd(arr: list):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    sum_even = 0
    product_odd = 1

    for number in arr:
        if number % 2 == 0:
            sum_even += number
        else:
            product_odd *= number

    return [sum_even, product_odd]

test_data = [1, 2, 3, 4]
print(sum_even_and_product_odd(test_data))



#2. Sum between range values
#You are given an array of integers and two integer values, min and max.
#Your task is to write a function that finds the sum of all elements in the
#array that fall within the range [min, max], inclusive.

def sum_between_range(arr: list, min_val: int, max_val: int):
    result = 0
    for number in arr:
        if number >= min_val and number <= max_val:
            result =+ number
    return result



test_arr = [3, 2, 1, 4, 10, 8]
test_min_val = 3
test_max_val = 7

print(sum_between_range(()))


#3. Stock price 2
#You are given an array of prices where prices[i] is the price of a given
#stock on the ith day. Find the maximum profit you can achieve.
#You may complete as many transactions as you like (buy one and sell one
# share of the stock multiple times).
# Define a function that takes a list of stock prices as its argument

def buy_and_sell_stock(prices: list):
    # Initialize the variable 'maximum' to store the maximum profit, starting at 0
    maximum = 0

    # Loop through the list of prices; stop one element before the last to avoid index out-of-bounds

# Check if the next day's price is higher than the current day's

# If it is, add the difference between the two prices to 'maximum'

# Return the calculated maximum profit after the loop ends

#4. Increment a Number
#Write a program that takes as input a list of digits encoding a non-negative
# decimal integer D and updates the list to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the list to [1, 3, 0].

def plus_one(arr: list):
    # Add 1 to the last digit of the number
    arr[-1] += 1

    # Loop through the array in reverse, starting from the second last element
    for i in reversed(range(1, len(arr))):

        # If the current digit is not 10, there's no carry-over, and we can break the loop
        if arr[i] != 10:
            break
        else:
            arr[i] = 0
            arr[i-1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

    # Set the current digit to 0 because we have a carry-over

    # Add 1 to the preceding digit (i-1) to handle the carry-over

    # Check if the most significant digit (first digit) has a carry-over

    # Set the first digit to 1

    # Append a 0 to the array to handle the carry-over from the most significant digit

test_data = [1, 2, 9]
print(plus_one(test_data))