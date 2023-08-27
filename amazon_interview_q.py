#Create a function that will take a string as an input
#and return the 1st unique letter of a string.
#"google" => l
#How would you test it? How would you handle edge cases

def unique(string: str):
    string = string.lower()

    for l in string: # O(n)
        if string.count(l) == 1: # O(n)
            return l
        #On^2

        #OR

def unique1(string2: str):
    string2 = string2.lower()
    d = {}
    for letter in string2: # O(n)
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    for k, v in d.items(): # O(n)
        if v == 1:
            return k
# O(n)

print(unique('Happy'))

print(unique1('Google'))