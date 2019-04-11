# practice 1. set's overlap
# Let's remove duplicate value from following list 'a' using feature of the set data that do not allow duplicates.
a = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5]
aSet = set(a)  # Duplicates are removed.
b = list(aSet)  # Transform set to list
print(b)
