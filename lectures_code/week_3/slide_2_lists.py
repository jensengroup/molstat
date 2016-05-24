# Example: Copy of lists

# TODO
# Explain 'view' on whiteboard
# Explain 'pointer'/ID to RAM

# float example
a = 5.0
b = a
a = 6.0
print "a", a
print "b", b

# List example
a_list = [1.0, 2.0, 3.0]
b_list = a_list
a_list[0] = 5.0
print "a", a_list
print "b", b_list

# Pointer / ID
print id(a_list)
print id(b_list)


# Copy example
import copy

a_list = [1.0, 2.0, 3.0]
b_list = copy.copy(a_list)
a_list[0] = 5.0
print "a", a_list
print "b", b_list
print id(a_list)
print id(b_list)


