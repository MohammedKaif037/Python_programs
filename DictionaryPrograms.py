# 1. Counting Letter Frequency

# Write a program to count the frequency of each letter in a given string.

def count_letter_frequency(string):
    frequency = {}
    for letter in string:
        if letter.isalpha():
            letter = letter.lower()
            frequency[letter] = frequency.get(letter, 0) + 1
    return frequency

string = "Hello, World!"
print(count_letter_frequency(string))


# 2. Merge Dictionaries

# Write a program to merge two dictionaries into a single dictionary.

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(merge_dictionaries(dict1, dict2))


# 3. Sorting Dictionary by Value

# Write a program to sort a dictionary by its values.

def sort_dictionary_by_value(dictionary):
    sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
    return sorted_dict

dictionary = {"a": 3, "b": 1, "c": 2}
print(sort_dictionary_by_value(dictionary))


# 4. Finding Common Keys

# Write a program to find common keys between two dictionaries.

def find_common_keys(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    return common_keys

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
print(find_common_keys(dict1, dict2))


# 5. Removing Duplicates from Dictionary

# Write a program to remove duplicate values from a dictionary.

def remove_duplicates(dictionary):
    unique_values = list(set(dictionary.values()))
    unique_dict = {key: value for key, value in dictionary.items() if value in unique_values}
    return unique_dict

dictionary = {"a": 1, "b": 2, "c": 2, "d": 3}
print(remove_duplicates(dictionary))


# 6. Counting Word Frequency in a Text

# Write a program to count the frequency of each word in a given text.

def count_word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

text = "This is a sample text. This text is used for testing purposes."
print(count_word_frequency(text))


# 7. Finding Maximum and Minimum Value in a Dictionary

# Write a program to find the maximum and minimum value in a dictionary.

def find_max_min_values(dictionary):
    values = list(dictionary.values())
    max_value = max(values)
    min_value = min(values)
    return max_value, min_value

dictionary = {"a": 10, "b": 5, "c": 8, "d": 3}
print(find_max_min_values(dictionary))


# 8. Checking Dictionary Equality

# Write a program to check if two dictionaries are equal.

def check_dictionary_equality(dict1, dict2):
    return dict1 == dict2

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2}
print(check_dictionary_equality(dict1, dict2))


# 9. Counting Vowels in a String using Dictionary

# Write a program to count the number of vowels in a given string using a dictionary.

def count_vowels(string):
    vowels = "aeiou"
    count = {}
    for char in string.lower():
        if char in vowels:
            count[char] = count.get(char, 0) + 1
    return count

string = "Hello, World!"
print(count_vowels(string))


# 10. Merging Dictionaries with Common Keys

# Write a program to merge two dictionaries by adding their values for common keys.

def merge_dictionaries_with_common_keys(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
print(merge_dictionaries_with_common_keys(dict1, dict2))


# 11. Finding Longest Key in Dictionary

# Write a program to find the longest key in a dictionary.

def find_longest_key(dictionary):
    longest_key = max(dictionary.keys(), key=len)
    return longest_key

dictionary = {"apple": 3, "banana": 2, "cherry": 5}
print(find_longest_key(dictionary))


# 12. Checking if a Key Exists in Dictionary

# Write a program to check if a given key exists in a dictionary.

def check_key_existence(dictionary, key):
    return key in dictionary

dictionary = {"a": 1, "b": 2, "c": 3}
key = "b"
print(check_key_existence(dictionary, key))


# 13. Reversing Dictionary Key-Value Pairs

# Write a program to reverse the key-value pairs of a dictionary.

def reverse_dictionary(dictionary):
    reversed_dict = {value: key for key, value in dictionary.items()}
    return reversed_dict

dictionary = {"a": 1, "b": 2, "c": 3}
print(reverse_dictionary(dictionary))


# 14. Checking if Dictionary is Empty

# Write a program to check if a dictionary is empty.

def check_dictionary_empty(dictionary):
    return not bool(dictionary)

dictionary = {}
print(check_dictionary_empty(dictionary))


# 15. Finding Common Values

# Write a program to find common values between two dictionaries.

def find_common_values(dict1, dict2):
    common_values = set(dict1.values()) & set(dict2.values())
    return common_values

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 3}
print(find_common_values(dict1, dict2))


# 16. Nested Dictionary Sorting

# Write a program to sort a nested dictionary by a specific key.

def sort_nested_dictionary(nested_dict, key):
    sorted_dict = {k: v for k, v in sorted(nested_dict.items(), key=lambda item: item[1][key])}
    return sorted_dict

nested_dict = {"a": {"name": "John", "age": 25}, "b": {"name": "Alice", "age": 30}, "c": {"name": "Bob", "age": 20}}
key = "age"
print(sort_nested_dictionary(nested_dict, key))


# 17. Removing Keys with None Values

# Write a program to remove keys with None values from a dictionary.

def remove_none_values(dictionary):
    cleaned_dict = {key: value for key, value in dictionary.items() if value is not None}
    return cleaned_dict

dictionary = {"a": 1, "b": None, "c": 3, "d": None}
print(remove_none_values(dictionary))


# 18. Converting List of Dictionaries to Dictionary

# Write a program to convert a list of dictionaries into a single dictionary.

def convert_list_of_dictionaries(list_of_dicts):
    merged_dict = {}
    for dictionary in list_of_dicts:
        merged_dict.update(dictionary)
    return merged_dict

list_of_dicts = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
print(convert_list_of_dictionaries(list_of_dicts))


# 19. Finding Key with Maximum Value

# Write a program to find the key with the maximum value in a dictionary.

def find_key_with_max_value(dictionary):
    max_value = max(dictionary.values())
    max_keys = [key for key, value in dictionary.items() if value == max_value]
    return max_keys

dictionary = {"a": 10, "b": 5, "c": 10, "d": 3}
print(find_key_with_max_value(dictionary))


# 20. Checking if Dictionary is a Subset of Another Dictionary

# Write a program to check if a dictionary is a subset of another dictionary.

def check_dictionary_subset(dict1, dict2):
    return all(item in dict2.items() for item in dict1.items())

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}
print(check_dictionary_subset(dict1, dict2))
