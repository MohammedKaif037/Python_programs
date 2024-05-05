
# 1. Program to find the maximum and minimum values in a tuple:

def find_min_max(t):
    return min(t), max(t)

tuple_1 = (1, 5, 3, 8, 2)
min_value, max_value = find_min_max(tuple_1)
print("Minimum value:", min_value)
print("Maximum value:", max_value)


# 2. Program to merge two tuples into a single sorted tuple:

def merge_tuples(t1, t2):
    merged = sorted(t1 + t2)
    return tuple(merged)

tuple_1 = (1, 3, 5)
tuple_2 = (2, 4, 6)
merged_tuple = merge_tuples(tuple_1, tuple_2)
print("Merged tuple:", merged_tuple)


# 3. Program to remove duplicate elements from a tuple:

def remove_duplicates(t):
    return tuple(set(t))

tuple_1 = (1, 2, 3, 3, 4, 5, 5)
unique_tuple = remove_duplicates(tuple_1)
print("Unique tuple:", unique_tuple)


# 4. Program to check if a tuple contains all elements of another tuple:

def contains_all_elements(t1, t2):
    return all(elem in t1 for elem in t2)

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (3, 4)
result = contains_all_elements(tuple_1, tuple_2)
print("Contains all elements:", result)


# 5. Program to count the occurrences of an element in a tuple:

def count_occurrences(t, element):
    return t.count(element)

tuple_1 = (1, 2, 3, 2, 4, 2, 5)
element = 2
count = count_occurrences(tuple_1, element)
print("Occurrences of", element, ":", count)


# 6. Program to find the index of the first occurrence of an element in a tuple:/

def find_first_index(t, element):
    return t.index(element)

tuple_1 = (1, 2, 3, 2, 4, 2, 5)
element = 2
index = find_first_index(tuple_1, element)
print("First index of", element, ":", index)


# 7. Program to find the common elements between two tuples:

def find_common_elements(t1, t2):
    return tuple(set(t1) & set(t2))

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (4, 5, 6, 7)
common_elements = find_common_elements(tuple_1, tuple_2)
print("Common elements:", common_elements)


# 8. Program to convert a tuple to a dictionary:

def convert_to_dictionary(t):
    dictionary = {}
    for i, elem in enumerate(t):
        dictionary[i] = elem
    return dictionary

tuple_1 = (1, 2, 3, 4, 5)
dictionary = convert_to_dictionary(tuple_1)
print("Dictionary:", dictionary)


# 9. Program to check if a tuple is a subset of another tuple:

def is_subset(t1, t2):
    return set(t1).issubset(set(t2))

tuple_1 = (1, 2, 3)
tuple_2 = (1, 2, 3, 4, 5)
result = is_subset(tuple_1, tuple_2)
print("Is subset:", result)


# 10. Program to find the largest and smallest N elements from a tuple:

def find_largest_smallest_n(t, n):
    largest = sorted(t)[-n:]
    smallest = sorted(t)[:n]
    return tuple(largest), tuple(smallest)

tuple_1 = (5, 2, 8, 3, 1, 6, 9)
n = 3
largest_n, smallest_n = find_largest_smallest_n(tuple_1, n)
print("Largest", n, "elements:", largest_n)
print("Smallest", n, "elements:", smallest_n)
