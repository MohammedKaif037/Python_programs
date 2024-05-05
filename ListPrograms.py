# 1. Find the Maximum and Minimum Values in a List

def find_max_min(lst):
    max_value = max(lst)
    min_value = min(lst)
    return max_value, min_value

numbers = [10, 5, 20, 15, 30]
max_num, min_num = find_max_min(numbers)
print("Maximum value:", max_num)
print("Minimum value:", min_num)


# 2. Remove Duplicates from a List

def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 3, 4, 2, 3, 5, 6, 3, 4]
unique_numbers = remove_duplicates(numbers)
print("List with duplicates removed:", unique_numbers)


# 3. Sort a List in Descending Order

def sort_descending(lst):
    return sorted(lst, reverse=True)

numbers = [5, 2, 8, 1, 6]
sorted_numbers = sort_descending(numbers)
print("Sorted list in descending order:", sorted_numbers)


# 4. Count the Frequency of Elements in a List

def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

numbers = [1, 2, 3, 2, 1, 3, 4, 2, 5]
frequency_count = count_frequency(numbers)
print("Frequency count:", frequency_count)


# 5. Reverse a List

def reverse_list(lst):
    return lst[::-1]

numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print("Reversed list:", reversed_numbers)


# 6. Find the Second Largest Element in a List

def find_second_largest(lst):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[1]

numbers = [10, 5, 20, 15, 30]
second_largest = find_second_largest(numbers)
print("Second largest element:", second_largest)


# 7. Check if a List is Palindrome

def is_palindrome(lst):
    reversed_list = lst[::-1]
    return lst == reversed_list

words = ['level', 'python', 'radar', 'hello']
for word in words:
    if is_palindrome(word):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")


# 8. Find the Union of Two Lists

def find_union(lst1, lst2):
    return list(set(lst1).union(set(lst2)))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
union_list = find_union(list1, list2)
print("Union of two lists:", union_list)


# 9. Find the Intersection of Two Lists

def find_intersection(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection_list = find_intersection(list1, list2)
print("Intersection of two lists:", intersection_list)


# 10. Find the Sum of Odd Numbers in a List

def sum_odd_numbers(lst):
    return sum([num for num in lst if num % 2 != 0])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_sum = sum_odd_numbers(numbers)
print("Sum of odd numbers:", odd_sum)
