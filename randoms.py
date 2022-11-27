import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?

# I can see the code trying to generate a random number,
# which would be Return a number between 5 and 20 (5 and 20 inclusive):

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?

# The code will randomly try to generate odd numbers within 3 to 10
# 5/9
# The code does not generate 4, because it follows the above rule.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?

# This code tries to generate a regular floating point number
# with a minimum of 2.5 and a maximum of infinitely close to 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1, 100))