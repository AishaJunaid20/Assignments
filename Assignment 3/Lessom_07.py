# Lesson :07 Set and Frozenset 

# Normal set (mutable)
numbers = {1, 2, 3, 4, 5}
print("Set of Numbers:", numbers)

# Adding an element (Allowed in set)
numbers.add(6)
print("Updated Set:", numbers)

# Creating a frozenset (immutable set)
frozen_numbers = frozenset({10, 20, 30, 40})
print("Frozen Set:", frozen_numbers)

# Attempting to modify a frozenset (This will cause an error)
# frozen_numbers.add(50)  # ❌ Not allowed

# Set Operations with frozenset
union_set = numbers.union(frozen_numbers)  # Allowed
intersection_set = numbers.intersection(frozen_numbers)  # Allowed

print("Union with Frozen Set:", union_set)
print("Intersection with Frozen Set:", intersection_set)
