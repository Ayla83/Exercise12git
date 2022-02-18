# What is going on here?  Can you explain the output?

tup = 'Hello'
print(len(tup))

# Here, tup is a string, so len returns a value of 5 since the string contains 5 characters.

tup = 'Hello',
print(len(tup))

# Here, len is a tuple, due to the trailing comma, with a single element of 'Hello', so that len returns 1.
