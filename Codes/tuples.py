# Characteristics of Tuples
# They are indexed.
# Tuples are ordered.
# These are immutable.
# They can contain duplicate items.

# Empty Tuple

tuple_empty = ()
print(tuple_empty)


our_tuple = (1, 2, 3)
print(our_tuple)


our_tuple = ("python", "lesson", 1)

print(our_tuple)

my_tuple = (1, 2, 3, 4, 5)
x, y, *rest = my_tuple
print(x, y, rest)
