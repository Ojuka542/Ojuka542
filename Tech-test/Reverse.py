# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reverse_integer(num):
    sign = -1 if num < 0 else 1
    reversed_num = sign * int(str(abs(num))[::-1])
    return reversed_num
print(reverse_integer(500))  
print(reverse_integer(-56))  
print(reverse_integer(-90))  
print(reverse_integer(91))   

