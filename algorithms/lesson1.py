# # manuel function
# def swap_variables(a, b):
#     print(f"a = {a}, b = {b}")
#     a, b = b, a
#     print(f"a = {a}, b = {b}")
#
# testa = 5
# testb = 10
# swap_variables(testa, testb)
#
# # built in function
# # def swap_variables(a, b):
# #     print(f"a = {a}, b = {b}")
# #     temp = a
# #     a = bb = temp
# #     print(f"a = {a}, b = {b}")
#
# def swap_var(c, d):
#     print(f"c = {c}, d = {d}")
#     # c, d = d, c
#     c = c + d
#     d = c - d
#     c = c - d
#     print(f"c = {c}, d = {d}")
#
#
# testc = 5
# testd = 10
#
# swap_var(testc, testd)
#
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
fizzbuzz()

def fizzbuzzn(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
fizzbuzzn(30)


def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    print(f'the factorial of {n} is {result}')

factorial(5)

def sum_of_three(number:int):
    result = 0
    for i in range(3):
        result = result + (number % 10)
        number = number // 10
    return result
test_result = sum_of_three(291)
print(test_result)

def reverse_string(s: str):
    print(s[::-1])

reverse_string('abcde')


#reverse integer:
def reverse_negative_number(n: int):
    string = str(n)
    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])

print(reverse_negative_number(-451))
print(reverse_negative_number(451))

def is_anagram(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(is_anagram(s1='cat', s2='tac'))

def is_palin(s: str):
    if s == s[::-1]:
        return True
    else:
        return False
print(is_anagram('racecar'))

#almost palindrome example rakdar
def almost_palindrom(s: str):
    word = len(s)
    for i in range(word):
        new_s = s[:i] + s[i + 1:]
        if new_s == new_s[::-1]:
            return True
    return False
print(almost_palindrom('rakdar'))


