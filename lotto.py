# Generate and display 6 unique random lottery numbers between 1 and 50.
# Which python structure is best suited to store the numbers.
# Use python help() function to find out which function to use from the python standard library called random.

# import random
# help(random)

from random import sample

lotmin = 1
lotmax = 50
unique = 6
winner = sample(range(lotmin, lotmax+1), unique)
print("This week's winning lottery numbers are: ", winner)

# range(a,b) includes a but stops at b and does not include it, necessitating tha addition of 1 to lotmax