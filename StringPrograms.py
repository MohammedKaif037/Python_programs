#1. Count the number of characters in a string

string = "Hello, World!"
count = len(string)
print("Number of characters:", count)


#2. Reverse a string

string = "Hello, World!"
reversed_string = string[::-1]
print("Reversed string:", reversed_string)


#3. Check if a string is a palindrome

string = "madam"
reversed_string = string[::-1]
if string == reversed_string:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


#4. Count the occurrences of a specific character in a string

string = "Hello, World!"
char = "l"
count = string.count(char)
print("Number of occurrences of", char, "in the string:", count)


#5. Remove all the spaces from a string

string = "Hello, World!"
no_spaces = string.replace(" ", "")
print("String with no spaces:", no_spaces)


#6. Convert a string to uppercase

string = "Hello, World!"
uppercase_string = string.upper()
print("Uppercase string:", uppercase_string)


#7. Check if a string starts with a specific substring

string = "Hello, World!"
substring = "Hello"
if string.startswith(substring):
    print("The string starts with", substring)
else:
    print("The string does not start with", substring)


#8. Split a string into a list of words

string = "Hello, World!"
words = string.split()
print("List of words:", words)


#9. Replace a specific substring in a string

string = "Hello, World!"
old_substring = "World"
new_substring = "Universe"
new_string = string.replace(old_substring, new_substring)
print("Updated string:", new_string)


#10. Check if a string is numeric

string = "42"
if string.isnumeric():
    print("The string is numeric")
else:
    print("The string is not numeric")
