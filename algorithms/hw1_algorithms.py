#Task 1. There is a program that prints the numbers from 1 to 100.
#If the number is divisible of 3, print “Bin”
#If the number is divisible of 7, print “Go”
#For numbers which are divisible of 3 and 7, print “BinGo”

def bingo():
    for i in range(1, 101):
        if i % 3 == 0 and i % 7 == 0:
            print('BinGo')
        elif i % 3 == 0:
            print('Bin')
        elif i % 7 == 0:
            print('Go')
        else:
            print(i)
bingo()

#Task 2. Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
def sum_numbers(n):
    final_sum = 0
    for i in range(1, n + 1):
        final_sum += i
    return final_sum

test1 = sum_numbers(5)
print(test1)

#Task 3. Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

def max_number_3(a: int, b: int, c: int):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

largest = max_number_3(3, 290, 49)
print(largest)

#Task 4. Leap year. When a function gets a year, the code
# detects if it is a leap year or not.
def leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year')
            else:
                print(f'{year} is not leap year')
        else:
            print(f'{year} is a leap year')
    else:
        print(f'{year} is not leap year')
leap_year(1987)
leap_year(2024)

#Fibonacci. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. Print out the Fibonacci sequence until the given n-th in the sequence.
#Example: n = 7, print out the sequence: 0, 1, 1, 2, 3, 5, 8
def generate_fibonacci_sequence(n: int):
    fib_sequence = [0, 1]
    for i in range(2, n):
        new_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(new_number)


    return fib_sequence
print(generate_fibonacci_sequence(7))
