# 1. Find the union of two sets:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}


# 2. Find the intersection of two sets:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}


# 3. Check if a set is a subset of another set:

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print(is_subset)  # Output: True


# 4. Find the difference between two sets:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}


# 5. Check if two sets are disjoint:

set1 = {1, 2, 3}
set2 = {4, 5, 6}
is_disjoint = set1.isdisjoint(set2)
print(is_disjoint)  # Output: True


# 6. Remove duplicates from a list using sets:

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)  # Output: [1, 2, 3, 4, 5]


# 7. Check if two sets are equal:

set1 = {1, 2, 3}
set2 = {3, 2, 1}
are_equal = set1 == set2
print(are_equal)  # Output: True


# 8. Find the symmetric difference between two sets:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # Output: {1, 2, 4, 5}


# 9. Check if a set is a proper subset of another set:

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_proper_subset = set1.issubset(set2) and set1 != set2
print(is_proper_subset)  # Output: True


# 10. Find the length of a set:

my_set = {1, 2, 3, 4, 5}
set_length = len(my_set)
print(set_length)  # Output: 5
