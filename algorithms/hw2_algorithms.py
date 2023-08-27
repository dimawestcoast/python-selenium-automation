#Task 1.  Reverse a negative integer and keep the negative sign at the beginning.
#Example: -189 -> -981
def reverse_negative_integer(n: int):
    string = str(n)
    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])

print(reverse_negative_integer(-198))

#Task 2. Write a function that takes two strings as input and returns True if they are anagrams of each other, and False otherwise.
#The strings can contain uppercase and lowercase letters, and should be ignored during the comparison.
def is_anagram(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(is_anagram('cat','tac'))
print(is_anagram('dog','fish'))

#Task 3. Given a sentence, reverse the order of characters in each word.
#Examples:
#“Hello World” should be transformed into “olleH dlroW”
#“mistertwister” should be transformed into “retsiwtretsim”
def reverse_words(sentence: str):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

sentence = 'Hello im Dmitriy'
result = reverse_words(sentence)
print(result)

#Task 4. Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.
#Examples:
#“312” should return “333122”
def repeat_digits(s: str):
    result = ""  # Initialize an empty string to store the result

    for char in s:  # Iterate through each character in the input string
        if char.isdigit():
            repeat_count = int(char)
            result += char * repeat_count
        else:
            result += char
    return result

print(repeat_digits('123'))

#Task 5. Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u) in a given string.
#“y” is not considered a vowel for this task. The input string is always in lowercase.

def shortcut(s: str):
    char_to_remove = 'aeiou'
    results = ""
    for char in s:
        if char not in char_to_remove:
            results += char
    return results

print(shortcut('hello'))





