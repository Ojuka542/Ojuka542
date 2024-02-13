

# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

def is_power_of_two(a):
    return a > 0 and (a & (a - 1)) == 0
print(is_power_of_two(8))  # returns True
print(is_power_of_two(6))  # returns False



